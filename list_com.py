
list1=['Name','age','Location']

list2 = [f'{val}:length:{len(val)}' for val in list1]

print(list2)

x=frozenset(list1)
print(x)