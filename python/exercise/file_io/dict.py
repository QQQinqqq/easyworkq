

word = str(input("Word:"))
f = open('dict_info/dict.txt')

for line in f:
    w = line.split(' ')[0]
    if w > word:
        print("not find")
        break
    elif w == word:
        print(line)
        break
else:
    print("not find")
f.close()
