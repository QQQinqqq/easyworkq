import random

num1 = random.randint(70,200)
num2 = random.randint(70,200)
num3 = random.randint(70,200)
num4 = random.randint(70,200)

num_max = num1
if(num2 > num_max):
    num_max = num2
if(num3 > num_max):
    num_max = num3
if(num4 > num_max):
    num_max = num4

print(str(num1)+","+str(num2)+","+str(num3)+","+str(num4))
print(str(num_max))