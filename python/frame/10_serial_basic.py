import serial
import time

def ReceiveData(serial):
    tmp_wait = serial.inWaiting()
    if tmp_wait == 0:
        print('no data')
        return ''
    data = serial.read(tmp_wait)
    data_hex = data.hex()
    data_str = ''
    for i in range(len(data_hex)):
        data_str += data_hex[i]
        if i%2 == 1:
            data_str += ' '
    return data_str.strip().upper()

ser = serial.Serial('com1', 9600, timeout=1)
frame = '68 0F 00 43 00 00 00 00 00 00 10 40 0D A0 16'
frame_list = frame.strip().split(' ')
for i in range(len(frame_list)):
    frame_list[i] = int(frame_list[i], 16)

send_data = bytes(frame_list)
ser.write(send_data)
time.sleep(0.5)
receive_data = ReceiveData(ser)
print(receive_data)

ser.close()
