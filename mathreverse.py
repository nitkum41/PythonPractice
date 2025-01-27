import math


##revrse a 4 digit number using math functions

num = int(input("enter a 4 digit number ?"))
count = 0
list1 = []
while True:
    r = num % 10
    num = math.floor(num / 10)  #floor captures remainder
    list1.append(r)
    count += 1
    if count ==4:
        break

print(list1)

# math.sqrt()