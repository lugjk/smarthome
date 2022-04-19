import requests
import json
import datetime

BASE = 'https://io.adafruit.com/api/v2/Frost984/feeds/'

# Switch data
response_switch = requests.get(BASE + 'group-project.bbc-switch/data')

print(response_switch.status_code)

data_switch = response_switch.json()

with open("./data/switch.json", "w") as outfile:
    json.dump(data_switch, outfile)

# Button data
response_button = requests.get(BASE + 'group-project.bbc-button/data')

print(response_button.status_code)

data_button = response_button.json()

with open("./data/button.json", "w") as outfile:
    json.dump(data_button, outfile)

# Temperature data
response_tem = requests.get(BASE + 'group-project.bbc-temp/data')

print(response_tem.status_code)

data_tem = response_tem.json()

with open("./data/temperature.json", "w") as outfile:
    json.dump(data_tem, outfile)