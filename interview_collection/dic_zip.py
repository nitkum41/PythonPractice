### convert two lists to dictionary

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dict1 = {}
# for k, v in zip(keys, values):
#     dict1[k] = v
#
# print(dict1)


for k in keys:
        for v in values:
            if k not in dict1 and v not in dict1.values():
                dict1[k]=v



print(dict1)