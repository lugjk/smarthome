def on_received_string(receivedString):
    serial.write_string(receivedString)
radio.on_received_string(on_received_string)

counter_sensor = 3
radio.set_group(1)
led.enable(True)

flagDict = {"Button": True, "Magnet": True}

buttonpin = DigitalPin.P1
magneticpin = DigitalPin.P2
ledpin = (DigitalPin.P4, DigitalPin.P5)
buzzerpin = DigitalPin.P6

ledstates = [(False, False), (False, True), (True, False)]
state = 0

def on_forever():
    global flagDict, ledstates, state
    # Single Button
    if NPNBitKit.button(buttonpin) != flagDict["Button"]:
        s = "!1:BUTTON:" + ("0" if flagDict["Button"] else "1") + "#"
        serial.write_string(s)
        if not flagDict["Button"]:
            basic.show_number(state)
            NPNBitKit.led2_color(ledpin[0], ledstates[state][0], ledpin[1], ledstates[state][1])
            state = (state + 1) % 3
        flagDict["Button"] = not flagDict["Button"]
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
        NPNBitKit.relay(DigitalPin.P6, num != 0)

serial.on_data_received(serial.delimiters(Delimiters.HASH), on_data_received)
