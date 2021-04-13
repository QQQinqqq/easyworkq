import serial

def ReceiveData(serial):
    tmp_wait = serial.inWaiting()
    if tmp_wait !=0：
        serial.read(tmp_wait)
    else:
        print('no data')

ser = serial.Serial('com1'，9600，timeout=1)
frame = '68 0F 00 43 00 00 00 00 00 00 10 40 0D A0 16'
frame_list = frame.strip().split(' ')
for i in range(len(frame_list)):
    frame_list[i] = int(frame_list[i], 16)

send_data = bytes(frame_list)
ser.write(send_data)
time.sleep(0.5)
receive_data = ReceiceData(ser)

ser.close()
