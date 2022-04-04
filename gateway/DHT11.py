def on_received_string(receivedString):
    serial.write_string(receivedString)
radio.on_received_string(on_received_string)

counter_sensor = 0
radio.set_group(1)
led.enable(True)
# radio.send_string("!1:TEMP:" + str(input.temperature()) + "#")
# basic.pause(30000)

def on_forever():
    NPNBitKit.dht11_read(DigitalPin.P3)
    serial.write_string("!1:TEMP:" + ("" + str(NPNBitKit.dht11_temp())) + "#")
    basic.show_string("!1:TEMP:" + ("" + str(NPNBitKit.dht11_temp()) + "#"))
basic.forever(on_forever)
