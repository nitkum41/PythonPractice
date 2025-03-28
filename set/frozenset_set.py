my_dict = {frozenset({1, 2}): 'value'}
print(my_dict)



import sys

s = {1, 2, 3, 4, 5,1,8,9}
fs = frozenset(s)

print(s,fs)

print(sys.getsizeof(s))  # output: 736
print(sys.getsizeof(fs)) # output: 224