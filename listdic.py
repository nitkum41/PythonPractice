list_dic = [{'first': 111111},
            {'second': 222},
            {'third': 3333},
            {'another': 4444444},
            {'second': 222},
            {'one': 333}]
# using for loop
""" 
res_list = []
for i in range(len(list_dic)):
    if list_dic[i] not in list_dic[i+1:]:
        res_list.append(list_dic[i])
print(res_list)
"""

# using list comprehension
"""

res_list = [v for k, v in enumerate(list_dic) if v not in list_dic[k+1:]]
print(res_list)

"""

# using frozenset

res_list = {frozenset(item.items()): item for item in list_dic}.values()
print(list(res_list))



