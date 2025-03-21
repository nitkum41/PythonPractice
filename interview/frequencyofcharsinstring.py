import collections
from collections import Counter

str1= "amazon.com"

#metod 1
count_dict = Counter(str1)
print(count_dict)


##method2
count_dict ={}

# for char in str1:
#     if char not in count_dict:
#         count_dict[char]=1
#     else:
#         count_dict[char]+=1
# print(count_dict)
