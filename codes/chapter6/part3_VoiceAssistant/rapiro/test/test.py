import serial
ser = serial.Serial('/dev/ttyUSB0', 57600, timeout=1)
#ser.open()

ser.write(b"#M2")
try:
    while 1:
        response = ser.readline()
        print(response)
except KeyboardInterrupt:
    ser.close()
