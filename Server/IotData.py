import requests
from datetime import datetime, timedelta

BASE = 'https://io.adafruit.com/api/v2/Frost984/feeds/'
# TEMP = "group-project.bbc-temp"
# BUZZER = "group-project.bbc-buzzer"

def requestDataAdafruit(device, start_time = None, end_time = None, limit = None):
    req = BASE + device + '/data?'
    if start_time: req += f'start_time={start_time}' 
    if end_time: req += f'&end_time="{end_time}"'
    if limit: req += f'&limit="{limit}"'
    response = requests.get(req).json()
    return [(ele["value"], ele["created_at"]) for ele in response]

def getActiveTimeSwitch(devicecode ,start_time, end_time):
    data = requestDataAdafruit(devicecode, start_time, end_time)
    value = requestDataAdafruit(devicecode, end_time=start_time, limit=1)[0][0]
    start = datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%SZ")
    totalTime = timedelta()

    for v, t in data[::-1]:
        if value != v:
            t = datetime.strptime(t, "%Y-%m-%dT%H:%M:%SZ") 
            if value == "1":
                totalTime += t - start
            value = v
            start = t
    if value == "1":
        totalTime += datetime.strptime(end_time, "%Y-%m-%dT%H:%M:%SZ") - start

    return totalTime

# def getTemp(start_time, end_time):
#     data = requestDataAdafruit(TEMP, start_time, end_time)
#     value = requestDataAdafruit(TEMP, end_time=start_time, limit=1)[0][0]

#     result = [{"value": value, "time_created": start_time}]

#     for v, t in data[::-1]:
#         if v != value:
#             value = v
#             result.append({"value": value, "time_created": t})
    
#     result.append({"value": value, "time_created": end_time})
#     return result
            