flagDict = {"Button": True, "Magnet": True}

def on_forever():
    global flagDict

    # Single Button
    if NPNBitKit.button(DigitalPin.P2) != flagDict["Button"]:
        s = "!1:BUTTON:" + ("0" if flag else "1") + "#"
        serial.write_string(s)
        flagDict["Button"] = not flagDict["Button"]
    
    # DHT11
    NPNBitKit.dht11_read(DigitalPin.P3)
    serial.write_string("!1:TEMP:" + ("" + str(NPNBitKit.dht11_temp())) + "#")
    basic.show_string("!1:TEMP:" + ("" + str(NPNBitKit.dht11_temp()) + "#"))
    
    # Magnetic switch
    if NPNBitKit.button_door_open(DigitalPin.P4) != flagDict["Magnet"]:
        s = "!1:MAGNETIC:" + ("0" if flagDict["Magnet"] else "1") + "#"
        serial.write_string(s)
        flagDict["Magnet"] = not flagDict["Magnet"]


basic.forever(on_forever)