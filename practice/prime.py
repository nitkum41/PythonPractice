list_p = [2]


for num in range(3, 100, 2):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            break
    else:
        list_p.append(num)

print(len(list_p))
print(list_p)
