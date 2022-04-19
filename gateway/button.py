def on_received_string(receivedString):
    serial.write_string(receivedString)
radio.on_received_string(on_received_string)

counter_sensor = 0
radio.set_group(1)
led.enable(True)
# basic.show_string(s)

flag = True
def on_forever():
    global flag
    if NPNBitKit.button(DigitalPin.P2) != flag:
        s = "!1:BUTTON:" + ("0" if flag else "1") + "#"
        serial.write_string(s)
        flag = not flag
  
basic.forever(on_forever)
