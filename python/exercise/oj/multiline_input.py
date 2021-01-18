def func():
    content = []
    while True:
        try:
            line = input("")
            content.append(line)
        except EOFException:
            break
        if line == "":
            break

    for strline in content:
        option = strline.split(" ")
        if len(option) == 2:
            print(int(option[0]) + int(option[1]))

if __name__ == '__main__':
    func() 
