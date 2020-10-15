import os
from functools import partial

#original send_message
def send_message(msg, chat_id, bot_token):
    ...

send_message = partial(send_message, 
                       chat_id=os.environ['CHAT_ID'], 
                       bot_token=os.environ['TELE_BOT_TOKEN'])

# to sends message to your bot.
send_message('hello to you bot!') 
