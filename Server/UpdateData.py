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
    listDevice = [{"_id":d["_id"], "name":d["name"]} for d in Devices().get_all()]
    now = datetime.now()
    now_ = now - timedelta(hours=7)
    start = (now_ - timedelta(minutes=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
    end = now_.strftime("%Y-%m-%dT%H:%M:%SZ")
    # print(type(getActiveTimeSwitch(listDevice[0], start, end)))
    col.insert_many([
        {
            "Sensor": d["_id"],
            "Timestamp": now,
            "Value": str(getActiveTimeSwitch(d["name"], start, end))
        }
        for d in listDevice
    ]) 

# schedule.every().day.at("00:00").do(job)
schedule.every(1).minutes.do(updateData)

def loopUpdate():
    while True:
        schedule.run_pending()
    
# loopUpdate()