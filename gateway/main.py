import sys
import random
import time
from Adafruit_IO import MQTTClient
import serial.tools.list_ports

ADAFRUIT_FEED_ID = ["group-project.bbc-relay", "group-project.bbc-buzzer", "group-project.bbc-led"]
ADAFRUIT_TEMP_FEED_ID = "group-project.bbc-temp"
ADAFRUIT_SWITCH_FEED_ID = "group-project.bbc-switch"
ADAFRUIT_BUTTON_FEED_ID = "group-project.bbc-button"

ADAFRUIT_IO_USERNAME = "Frost984"
ADAFRUIT_IO_KEY = "aio_qJaZ10pZlJnQMxtSk5tDB3v4NYj6"

PORT_NAME = "COM4"  #Replace this with the find port function in the book when we don't use the emulator

def connected(client):
    print("Connected succesfully")
    for id in ADAFRUIT_FEED_ID:
        client.subscribe(id)


def subscribe(client, userdata, mid, granted_qos):
    print("Subcribed")

def disconnected(client):
    print("Disconnected from Adafruit IO")
    sys.exit(1)

def make_payload(id, name, data):
    return f"!{id}:{name}:{data}#"

def message(client, feed_id, payload):
    print(f"Data received from feed {feed_id}: {payload}")
    #Add an if-else here to compare feed_id and make a proper payload for serial
    if feed_id == "group-project.bbc-relay":
        serial_payload = make_payload("3", "RELAY", payload)
    elif feed_id == "group-project.bbc-buzzer":
        serial_payload = make_payload("2", "SPEAKER", payload)
    elif feed_id == "group-project.bbc-led":
        serial_payload = make_payload("1", "LED", payload)
    else:
        return
    print(f"Serial payload: {serial_payload}")
    ser.write(serial_payload.encode())

def processData(data):
    print(f"Data from serial: {data}")
    data = data.replace("!", "")
    data = data.replace("#", "")
    try:
        (id, field, value) = data.split(":")
        if field == "TEMP-HUMID":
            (temp, humid) = value.split("-")
            client.publish(ADAFRUIT_TEMP_FEED_ID, temp)
        elif field == "BUTTON":
            client.publish(ADAFRUIT_BUTTON_FEED_ID, value)
        elif field == "MAGNETIC":
            client.publish(ADAFRUIT_SWITCH_FEED_ID, value)
    except ValueError:
        print(f"Data format error: {data}")


def getPort():
    ports = serial.tools.list_ports.comports()
    N = len(ports)
    commPort = "None"
    for i in range(0, N):
        port = ports[i]
        strPort = str(port)
        if "USB Serial Device" in strPort:
            splitPort = strPort.split(" ")
            commPort = (splitPort[0])
    return commPort

ser = serial.Serial(port=getPort(), baudrate=115200)
if (ser != None):
    print("Serial connected")
    isMicrobitConnected = True
else:
    isMicrobitConnected = False

mess = ""
def readSerial():
    bytesToRead = ser.inWaiting()
    global mess
    if (bytesToRead > 0):
        mess = mess + ser.read(bytesToRead).decode("utf-8")
        while ("#" in mess) and ("!" in mess):
            start = mess.find("!")
            end = mess.find("#")
            processData(mess[start:end+1])
            if (end == len(mess)):
                mess = ""
            else:
                mess = mess[end + 1:]


client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

while True:
    if isMicrobitConnected:
        readSerial()
    time.sleep(1)

