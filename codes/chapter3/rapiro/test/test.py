import serial
ser = serial.Serial('/dev/ttyUSB0', 57600, timeout=1)
#ser.open()

ser.write(b"#M2")
try:
    while 1:
        rESPonse = ser.readline()
        print(rESPonse)
except KeyboardInterrupt:
    ser.close()
