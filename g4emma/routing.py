from channels.routing import route
import g4emma.consumers as G4_consumers

channel_routing = [
    route("websocket.connect", G4_consumers.ws_connect),
    route("websocket.receive", G4_consumers.ws_message),
    route("websocket.disconnect", G4_consumers.ws_disconnect),
    route("sim_start_channel", G4_consumers.simulate),
]
