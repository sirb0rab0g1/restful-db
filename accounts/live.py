from channels import Group
from channels.sessions import channel_session


# Connected to websocket.connect
@channel_session
def ws_connect(message):
    # Accept connection
    message.reply_channel.send({"accept": True})
    # Work out game name from path (ignore slashes)
    game = message.content['path'].strip("/")
    # Save game in session and add us to the group
    message.channel_session['game'] = game
    Group("%s" % game).add(message.reply_channel)


# Connected to websocket.receive
@channel_session
def ws_message(message):
    print(message)
    Group("%s" % message.channel_session['game']).send({
        "text": message['text'],
    })


# Connected to websocket.disconnect
@channel_session
def ws_disconnect(message):
    Group("chat-%s" % message.channel_session['game']).discard(message.reply_channel)
