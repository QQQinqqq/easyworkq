import os

a = os.path.getsize("file_2021011701.txt") #returnhow many bytes
print(a)

a = os.listdir(".") #return file list
print(a)

a = os.path.exists("file_2021011701.txt")#return bool type
print(a)

a = os.path.isfile("dict_info")
print(a)

a = os.remove("file_2021011701.txt")
