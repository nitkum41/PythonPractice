list_p = [2]


def list_of_primes(number):
    for num in range(3, number+1, 2):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            list_p.append(num)
    return list_p

# print(len(list_p))
# print(list_p)

list_prims = list_of_primes(1000)

print(len(list_prims))

print(f"list of primes till {100} : {list_prims}")
