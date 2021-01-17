"""
overview: os use buffer to read and write data in disk, so if you want write data immediately, you must sync file.

update buffer:
    1.buffer is full
    2.program is finished or file object is closed
    3.buffering type is 1, which means line buffer, then meet newline
    4.call flush() in program

"""

f = open("file_20210117.txt",'w')
#f = open("file_20210117.txt",'w',1) #line buffer
while True:
    data = input(">>")
    if not data:
        break
    f.write(data)
#    f.write(data+'\n') #line buffer
    f.flush()

f.close()
