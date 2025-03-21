


# Key, Value of the dictionary defined
d = {'watermelon': 1, 'apple': 2, 'banana': 3}

# Sort based on Values
val_based = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
# item[1] represents the sorting based on value

# Sort based on reverse of Values
val_based_rev = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}

# Print sorted dictionary
print(val_based)
print(val_based_rev)













## sort using keys and values
dict1 ={
"a":5,
    "d":2,
    "b":7,
    "z":8
}

res1=sorted(dict1.items(),key= lambda i:i[0])
print(res1)



# Creates a sorted dictionary (sorted by key)
from collections import OrderedDict

d = {'ravi': '10', 'rajnish': '9', 'abc': '15'}
d1 = OrderedDict(sorted(d.items()))
print(dict(d1))

