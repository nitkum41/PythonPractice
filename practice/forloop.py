list_p = []
for num in range(3, 100, 2):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        list_p.append(num)

print(len(list_p))
