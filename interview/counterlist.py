from collections import Counter


list1 = [1,2,4,5,2,4,2,24,8,9]

################## count value 2 in the list
print(list1.count(2))



###############counter returns a dictionary

dic = Counter(list1)

print(dic)
print(dic[2])