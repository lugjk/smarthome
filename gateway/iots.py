def on_received_string(receivedString):
    serial.write_string(receivedString)
radio.on_received_string(on_received_string)

counter_sensor = 3
radio.set_group(1)
led.enable(True)

flagDict = {"Button": True, "Magnet": True}

def on_forever():
    global flagDict

    # Single Button
    # if NPNBitKit.button(DigitalPin.P2) != flagDict["Button"]:
    #     s = "!1:BUTTON:" + ("0" if flagDict["Button"] else "1") + "#"
    #     serial.write_string(s)
    #     flagDict["Button"] = not flagDict["Button"]
    
    # DHT11
    serial.write_string("!1:TEMP:" + ("" + str(input.temperature())) + "#")
    NPNBitKit.dht11_read(DigitalPin.P5)
    serial.write_string("!1:TEMP:" + ("" + str(NPNBitKit.dht11_temp())) + "#")
    # basic.show_string("!1:TEMP:" + ("" + str(NPNBitKit.dht11_temp()) + "#"))
    basic.pause(1000)

    # Magnetic switch
    # if NPNBitKit.button_door_open(DigitalPin.P4) != flagDict["Magnet"]:
    #     s = "!1:MAGNETIC:" + ("0" if flagDict["Magnet"] else "1") + "#"
    #     serial.write_string(s)
    #     flagDict["Magnet"] = not flagDict["Magnet"]


basic.forever(on_forever)




#############

def on_received_string(receivedString):
    serial.write_string(receivedString)
radio.on_received_string(on_received_string)

counter_sensor = 3
radio.set_group(1)
led.enable(True)

flagDict = {"Button": True, "Magnet": True}

def on_forever():
    global flagDict

    # Single Button
    if NPNBitKit.button(DigitalPin.P2) != flagDict["Button"]:
        s = "!1:BUTTON:" + ("0" if flagDict["Button"] else "1") + "#"
        serial.write_string(s)
        flagDict["Button"] = not flagDict["Button"]
    basic.pause(100)
    
    # DHT11
    # if (time() ):
    serial.write_string("!1:TEMP:" + ("" + str(input.temperature())) + "#")
    # NPNBitKit.dht11_read(DigitalPin.P6)
    # serial.write_string("!1:TEMP:" + ("" + str(NPNBitKit.dht11_temp())) + "#")
    # basic.show_string("!1:TEMP:" + ("" + str(NPNBitKit.dht11_temp()) + "#"))

    basic.pause(100)
    # Magnetic switch
    if NPNBitKit.button_door_open(DigitalPin.P4) != flagDict["Magnet"]:
        s = "!1:MAGNETIC:" + ("0" if flagDict["Magnet"] else "1") + "#"
        serial.write_string(s)
        flagDict["Magnet"] = not flagDict["Magnet"]


basic.forever(on_forever)

