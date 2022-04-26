def on_data_received():
    global cmd, num, device_id
    cmd = serial.read_until(serial.delimiters(Delimiters.HASH))
    num = int(cmd[len(cmd) - 1])
    device_id = int(cmd[1])
    # basic.show_string(cmd[len(cmd)-1])
    if device_id == 1:
        if num == 0:
            NPNBitKit.led2_color(DigitalPin.P1, False, DigitalPin.P2, False)
        elif num == 1:
            NPNBitKit.led2_color(DigitalPin.P1, True, DigitalPin.P2, False)
        elif num == 2:
            NPNBitKit.led2_color(DigitalPin.P1, False, DigitalPin.P2, True)
    elif device_id == 2:
        NPNBitKit.buzzer(DigitalPin.P5, num != 0)
    elif device_id == 3:
        NPNBitKit.relay(DigitalPin.P6, num != 0)

serial.on_data_received(serial.delimiters(Delimiters.HASH), on_data_received)

device_id = 0
num = 0
cmd = ""
counter_sensor = 0
radio.set_group(1)
led.enable(True)