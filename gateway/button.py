def on_received_string(receivedString):
    serial.write_string(receivedString)
radio.on_received_string(on_received_string)

counter_sensor = 0
radio.set_group(1)
led.enable(True)
# basic.show_string(s)

def on_forever():
    NPNBitKit.button(DigitalPin.P2)
    if NPNBitKit.button(DigitalPin.P2):
        s = "!1:BUTTON:" + "1" + "#"
        serial.write_string(s)
        basic.pause(100)
        s = "!1:BUTTON:" + "0" + "#"
        serial.write_string(s)
basic.forever(on_forever)
