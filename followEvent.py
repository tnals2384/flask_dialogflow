from asyncio.windows_events import NULL
from pymongo import MongoClient
from flask import Flask, request
app = Flask(__name__)

client = MongoClient("mongodb+srv://hanieminha:performance888@haniemchatbot.pvxxz0o.mongodb.net/test")
db = client.chatbot
collection = db.performance

@app.route('/')
def hello():
    return 'hello world'
   
@app.route('/webhook',methods=['GET','POST'])
def webhook():

    return{
    "destination": "xxxxxxxxxx",
    "events": [
        {
        "replyToken": "nHuyWiB7yP5Zw52FIkcQobQuGDXCTA",
        "type": "follow",
        "mode": "active",
        "timestamp": 1462629479859,
        "source": {
            "type": "user",
            "userId": "U4af4980629..."
        },
        "webhookEventId": "01FZ74A0TDDPYRVKNK77XKC3ZR",
        "deliveryContext": {
            "isRedelivery": false
        }
        }
    ]
    }
if __name__ =='__main__':
    #port = int(os.getenv('PORT',80))
    app.run(host='0.0.0.0',port=5000)