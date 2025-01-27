list1 = [1, 2, 3, 4, 5, 6, 1, 2]

tup = (5, 6, 7, 8, 'dd')

list1.append(6)
print(len(list1))
print(len(tup))

set1 = {1, 2, 3, 4, '3', (1, 2, 3), 'abc'}
set1.add(5)

print(set1)

for i, v in enumerate(set1):
    print(f'index :{i} & value :{v}')
set2 = set('a')
print(set2)
