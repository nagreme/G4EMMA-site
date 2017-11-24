from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels import Channel, Group
from channels.sessions import http_session, channel_session
from channels.auth import channel_and_http_session_user_from_http

# Connected to websocket.connect
@http_session
@channel_session
def ws_connect(message):
    # Accept connection
    message.reply_channel.send({"accept": True})

    # Store the suer dir from the http session in the channel session
    message.channel_session['userdir'] = message.http_session['userdir']

    # Add them to their userdir Group
    Group(message.http_session['userdir']).add(message.reply_channel)


# Connected to websocket.receive
def ws_message(message):
    pass


# Connected to websocket.disconnect
@channel_session
def ws_disconnect(message):
    Group(message.channel_session['userdir']).discard(message.reply_channel)
