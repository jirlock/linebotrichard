from flask import Flask
from linebot import LineBotApi, WebhookParser
from linebot.models import TextSendMessage, TextMessage, MessageEvent
import os

channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)

app = Flask(__name__)

@app.route('/callback', methods=['POST'])
def callback():
	request.headers['X-Line-Signature']
	body = request.get_data(as_text=True)
	events = parser.parse(body, signature)
	for event in events:
		if not isinstance(event, MessageEvent):
			continue
		if not isinstance(event.message, TextMessage):
			continue
		line_bot_api.reply_message(event.reply_token, TextSendMessage(text=event.message.text))
	return 'OK'

if __name__ == '__main__':
	app.run()






