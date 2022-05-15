def on_received_string(receivedString):
    serial.write_string(receivedString)
radio.on_received_string(on_received_string)

counter_sensor = 3
radio.set_group(1)
led.enable(True)

flagDict = {"Button": True, "Magnet": True}
isAlarm = False

buttonpin = DigitalPin.P3
magneticpin = DigitalPin.P4
ledpin = (DigitalPin.P8, DigitalPin.P9)
buzzerpin = DigitalPin.P5
relaypin = (DigitalPin.P1, DigitalPin.P2)


def on_forever():
    global flagDict
    global isAlarm
    # Single Button
    if NPNBitKit.button(buttonpin) != flagDict["Button"]:
        s = "!1:BUTTON:" + ("0" if flagDict["Button"] else "1") + "#"
        serial.write_string(s)
        # if not flagDict["Button"] and flagDict["Magnet"]:
        #     NPNBitKit.buzzer(buzzerpin, False)
        #     NPNBitKit.led2_color(ledpin[0], False, ledpin[1], True)
        flagDict["Button"] = not flagDict["Button"]
        if flagDict["Button"]:
            isAlarm = not isAlarm
    basic.pause(100)
    
    # DHT11
    # if (time() ):
    # serial.write_string("!1:TEMP:" + ("" + str(input.temperature())) + "#")
    # NPNBitKit.dht11_read(DigitalPin.P6)
    # serial.write_string("!1:TEMP:" + ("" + str(NPNBitKit.dht11_temp())) + "#")
    # basic.show_string("!1:TEMP:" + ("" + str(NPNBitKit.dht11_temp()) + "#"))

    basic.pause(100)
    # Magnetic switch
    
    if NPNBitKit.button_door_open(magneticpin) != flagDict["Magnet"]:
        s = "!1:MAGNETIC:" + ("0" if flagDict["Magnet"] else "1") + "#"
        serial.write_string(s)
        serial.write_string("!1:MAGNETIC:" + ("2" if isAlarm else "3") + "#")
        
        if not flagDict["Magnet"] and isAlarm:
            NPNBitKit.buzzer(buzzerpin, True)
            NPNBitKit.led2_color(ledpin[0], True, ledpin[1], False)
        else:
            NPNBitKit.buzzer(buzzerpin, False)
            NPNBitKit.led2_color(ledpin[0], False, ledpin[1], True)
        flagDict["Magnet"] = not flagDict["Magnet"]
        

basic.forever(on_forever)


##################################RECEIVE#############################
device_id = 0
num = 0
cmd = ""

def on_data_received():
    global cmd, num, device_id
    cmd = serial.read_until(serial.delimiters(Delimiters.HASH))
    num = int(cmd[len(cmd) - 1])
    device_id = int(cmd[1])
    # basic.show_string(cmd[len(cmd)-1])
    if device_id == 1:
        if num == 0:
            NPNBitKit.led2_color(ledpin[0], False, ledpin[1], False)
        elif num == 1:
            NPNBitKit.led2_color(ledpin[0], True, ledpin[1], False)
        elif num == 2:
            NPNBitKit.led2_color(ledpin[0], False, ledpin[1], True)
   
    elif device_id == 2:
        NPNBitKit.buzzer(buzzerpin, num != 0)
    elif device_id == 3:
        # if num == 0:
        #     NPNBitKit.led2_color(ledpin[0], False, ledpin[1], False)
        # elif num == 1:
        #     NPNBitKit.led2_color(ledpin[0], True, ledpin[1], False)
        # elif num == 2:
        #     NPNBitKit.led2_color(ledpin[0], False, ledpin[1], True)
        if num == 0:
            NPNBitKit.led2_color(relaypin[0], False, relaypin[1], False)
        elif num == 1:
            NPNBitKit.led2_color(relaypin[0], False, relaypin[1], True)
        # # NPNBitKit.relay(relaypin, num != 0)

serial.on_data_received(serial.delimiters(Delimiters.HASH), on_data_received)
