from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels import Channel, Group
from channels.sessions import http_session, channel_session, channel_and_http_session
from channels.auth import channel_and_http_session_user_from_http
from channels.security.websockets import allowed_hosts_only
import subprocess as sp
from pathlib import Path
import logging

stdlogger = logging.getLogger('django')


# Connected to websocket.connect
@channel_and_http_session
@allowed_hosts_only
def ws_connect(message):
    # Accept connection
    message.reply_channel.send({"accept": True})

    # Store the suer dir from the http session in the channel session
    message.channel_session['userdir'] = message.http_session['userdir']

    # Add them to their userdir Group
    Group(message.http_session['userdir']).add(message.reply_channel)


# Connected to websocket.receive
def ws_message(message):
    pass # trust no one


# Connected to websocket.disconnect
@channel_session
def ws_disconnect(message):
    Group(message.channel_session['userdir']).discard(message.reply_channel)
    # If simulation is on-going, it should be aborted when user disconnects
    # Not entirely sure how to do this, but this might be a good place for it



# Call the simulation wrapper on sim start msg
def simulate(message):

    command = message.content['cmd']

    print(command)

    stdlogger.info("About to call simulation wrapper: "+command)

    try:
        sp.check_call(command, shell=True)

    # Since I can't put information in the http session from here
    # I can't send back info about the type of error so there's no
    # point in having more specific except blocks here
    except Exception as e:
        stdlogger.exception(e)
        Group(message.content['userdir']).send({
            'text': "error",
        })

    # If there was no exception:
    else:
        stdlogger.info("Simulation completed without error")

        #If we make it out of there the sim end msg should be sent
        #TODO: Should I disable the management command that does the same thing?
        Group(message.content['userdir']).send({
            'text': "end",
        })
