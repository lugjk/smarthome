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
    listDevice = [d["name"] for d in Devices().get_all()]
    now = datetime.now()
    now_ = now - timedelta(hours=7)
    start = (now_ - timedelta(seconds=10)).strftime("%Y-%m-%dT%H:%M:%SZ")
    end = now_.strftime("%Y-%m-%dT%H:%M:%SZ")
    # print(type(getActiveTimeSwitch(listDevice[0], start, end)))
    col.insert_many([
        {
            "Sensor": d,
            "Timestamp": now,
            "Value": str(getActiveTimeSwitch(d, start, end))
        }
        for d in listDevice
    ]) 

# schedule.every().day.at("00:00").do(job)
schedule.every(10).seconds.do(updateData)

def loopUpdate():
    while True:
        schedule.run_pending()
    
# loopUpdate()