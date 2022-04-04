def on_received_string(receivedString):
    serial.write_string(receivedString)
radio.on_received_string(on_received_string)

counter_sensor = 0
radio.set_group(1)
led.enable(True)

def on_forever():
    if NPNBitKit.button(DigitalPin.P2):
        serial.write_string("!1:BUTTON:" + "1" + "#")
    else:
        basic.show_string("!1:BUTTON:" + "0" + "#")
basic.forever(on_forever)
