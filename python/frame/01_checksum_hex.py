def checksum(frame):
    sum = 0
    data_list = frame.strip().split(' ')
    for item in data_list:
        sum += int(item,16)

    return hex(sum%256+0x100)[-2:].upper()


def dec_list_2_frame(dec_list,if_invert=1,if_plus_33=0):
    frame = ''
    plus_33 = 0x33
    if if_plus_33 == 0:
        plus_33 = 0
    for i in range(len(dec_list)):
        if if_invert == 1:
            i = len(dec_list) - 1 - i
        frame += hex(int(str(dec_list[i]),16) + 0x100 + plus_33)[-2:] + ' '
    
    return frame.upper()

addr = [19,21,68,6,90,1]
addr_str = dec_list_2_frame(addr)
addr_33_str = dec_list_2_frame(addr,if_plus_33=1)

frame = '68 ' + addr_str + '68 ' + addr_33_str

check_sum = checksum(frame)
frame += check_sum + ' 16'
print(frame)
