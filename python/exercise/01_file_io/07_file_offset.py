#======== set position =======
f = open('file_20210117.txt','w+')

f.write("hello world")

data = f.read()

print("file offset:",f.tell())
f.seek(0,0) #set file offset to the beginning
#f.seek(-5,2)#open with binaray,and read last 5 char from current offset

data=f.read()
print(data)

f.close()

#======== reserve ========
f1 = open("file_2021011701.txt",'wb')
f1.write(b'a')
f1.seek(1024)
f1.write(b'b')

f1.close()

