import serial

ser = serial.Serial('com1', 115200, timeout=1)

ser.write(b'\r')
rcvdata = ser.readlines()

for line in rcvdata:
    print(line.decode())

a = 'ddeef'
ser.write(a.encode())
ser.write(b'\r')
rcvdata = ser.readlines()

for line in rcvdata:
    print(line.decode())
