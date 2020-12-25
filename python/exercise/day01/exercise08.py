dict01 = {"a":27,"b":29,"c":30}
iterator = dict01.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item,dict01[item])
    except StopIteration:
        break