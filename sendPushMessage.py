import os
import sys

from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

# get channel_access_token from your environment variable
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
userID = 'U553c02e0b0161bd0006af9a649095107'

tmp = input('Enter a message to send: ')
if(isinstance(tmp,str)) :
    line_bot_api.push_message(userID, TextSendMessage(text=tmp))

'''
while True :
    tmp = input('Enter a message to send: ')
    if(tmp!='q') :
        if(isinstance(tmp,str)) :
            line_bot_api.push_message('<userID>', TextSendMessage(text='hello'))
    else :
        break
'''