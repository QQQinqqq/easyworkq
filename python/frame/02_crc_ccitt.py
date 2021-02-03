def init_crc_table(num, polynomial=0x1021):
    crc = 0
    num = num << 8
    for i in range(8):
        if (crc ^ num) & 0x8000:
            crc = (crc << 1) ^ polynomial
        else:
            crc = crc << 1
        num = num << 1
    crc &= 0xffff

    return crc

crc_table = [ init_crc_table(i) for i in range(256) ]

def crc_ccitt(frame):
    crc = 0
    frame_list = frame.split(' ')

    for i in frame_list:
        tab_index = (crc >> 8) ^ (int(i,16) & 0xff) & 0xff
        crc = (crc << 8) ^ crc_table[tab_index]
        crc = crc & 0xffff

    return hex(crc)


frame = '48 80 01 00 00 00 08 00 48 53 21 39 0F 11 00 00'
crc = str(crc_ccitt(frame)).upper()
print("crc result: " + crc)
print(frame + ' ' + crc[2:4] + ' ' + crc[4:])
