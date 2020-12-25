distance = float(input("距离："))
init_speed = float(input("初速度："))
time = float(input("时间："))

acc = (distance - (init_speed * time)) * 2 / (time**2)

print("加速度：" + str(acc))
