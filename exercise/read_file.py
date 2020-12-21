"""
read file demo
"""

f = open('123.txt')

"""
while True:
    data = f.read(1024)
    if not data:
        break
    print(data)
"""

"""
while True:
    data = f.readline()
    if not data:
        break
    print(data,end="")
"""

"""
data = f.readlines()
print(data)
for i in data:
    print(i)
"""

for line in f:
    print(line)

f.close()
