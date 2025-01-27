# map

list1 = [4, 9, 5, 8, 2, 1, 7, 3, 6]
mo = map(lambda x: x * x, list1)  #map object taking in each value of list and passing into #lambda function
print(list(mo))

# filter

list2 = [4, 9, 5, 8, 2, 1, 7, 3, 6]
fo = filter(lambda x: x % 2 == 0, list2)
print(list(fo))


##iteration
go = iter(list1)  #generator object
print(len(list1))

try:
    for i in go:
        print('i :',i)
        print(type(i))
        # print(next(go)) ##move the pointer to next value and change the index
except StopIteration as e:
    print(e)