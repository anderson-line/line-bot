from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('jHTFpro/fuoLRDwl0yGRBfGT2v7Xr4tWLw0d0zh6mnzcb41Q3oSX0zmbDzVN1wZz3Xi23ntNL5EQzmdvxkFCdnYmOngnBi/esI/L45IGP8pyxImK5af1lcQCyG89BLMzEnvH1RIiFgj2vjTRoUr47wdB04t89/1O/w1cDnyilFU=')   #I put my TOKEN
handler = WebhookHandler('4f755a2f9e5814ac1a3fbfe98f8e2ed6')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = 'i can not undestand your msg'

    if msg in ['i']:
        r = 'i can hear you call me'
    elif msg in ['f','u','s']:
        r = 'you can not say bad word'
    elif msg == 'who are you' :
        r = 'i am a robot'
    elif msg in ['apex','Apex']:
        r = 'i want to play apex too'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()