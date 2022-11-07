from flask import Flask
from pymongo import MongoClient
import requests
import json
import xmltodict
client = MongoClient("mongodb+srv://hanieminha:performance888@haniemchatbot.pvxxz0o.mongodb.net/test")
db = client.chatbot
collection = db.performance
service_key = "301c5f567d2f41298b70c98de5d89b09"
params = {
    'service' : service_key,
    'ststype' : "day",
    'date' : 20221030
}

res = requests.get(url="http://kopis.or.kr/openApi/restful/boxoffice", params=params)
data = res.text
jsonString = json.dumps(xmltodict.parse(data), indent=4, ensure_ascii=False)

rankList = json.loads(jsonString)
rankArray = rankList["boxofs"]

ra=rankArray["boxof"]


for rank in ra:
    try:
        find_perfoID = rank["mt20id"]
        perfoRank = rank["rnum"]
        collection.update_one({"perfoID":find_perfoID},{"$set":{"rank":perfoRank}})
    except:
        continue