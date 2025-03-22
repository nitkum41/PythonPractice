### convert two lists to dictionary

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dict1 = {}
for k, v in zip(keys, values):
    dict1[k] = v

print(dict1)
