list_of_dic = {'first': 111111,
               'second': 222,
               'third': 3333,
               'another': 4444444,
               'last': 222,
               'one': 333 }


def func(item):
    return item[1]


# using sort function
# print(sorted(list_of_dic, key=func))

# merging dictionary

a = {'a':1}
b = {'b':2}
a.update(b)
print(a) #{'a': 1, 'b': 2}
