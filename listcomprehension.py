list1 = ['trrow', 'sorrow', 'deadly', 'humility']
list2 = [1, 2, 3, 4, 5, 6, 7, 8]

print(list1)

# reverse a list
# list1.reverse()
# print(list1)


##using sort reverse a list

# def func(item):
#     return item
#
# list1.sort(key=func)
# print(list1)



new_list = [val[::-1] for val in list1 if type(val) is str]  #reverse each item of the list

print(new_list)


# if else inside list comprehension


new_list1 = ['even' if val % 2 == 0 else 'odd' for val in list2]  #check value is odd or even
print(new_list1)



##nested for loop in list cpmprehension

new_list2 = [i for val in list1 for i in val]  #each value of each item in separate list
print(new_list2)
