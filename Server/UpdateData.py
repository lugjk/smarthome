import schedule
from IotData import *
from datetime import datetime, timedelta
import pymongo
from Models import Devices


client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.Smarthome
col = db.TimeUsed

def updateData():
    # Switch data
    # print(getSwitchData("2022-"))
    listDevice = [{"_id":d["_id"], "code":d["code"]} for d in Devices().get_all()]
    now = datetime.now()
    now_ = now - timedelta(hours=7)
    start = (now_ - timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
    end = now_.strftime("%Y-%m-%dT%H:%M:%SZ")
    # print(type(getActiveTimeSwitch(listDevice[0], start, end)))
    data = []
    for d in listDevice:
        v = getActiveTimeSwitch(d["code"], start, end)
        if v != timedelta():
            data.append({
                "Sensor": d["_id"],
                "Timestamp": now,
                "Value": str(v)
            })
    for d in data:
        print(d)
    if data:
        col.insert_many(data) 

schedule.every().day.at("00:05").do(updateData)
# schedule.every(30).minutes.do(updateData)

def loopUpdate():
    while True:
        schedule.run_pending()
    
# loopUpdate()