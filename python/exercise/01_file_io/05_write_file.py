# f = open('tmp1','w')

# f.write("123456")

# f = open('tmp1', 'wb')

# f.write(b"98765")

with open('tmp1','w+') as f:
    list1 = []
    for i in range(100,200):
        list1.append(str(i) + '\n')

    f.writelines(list1)

# f.close()
