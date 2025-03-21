mystring="aggregator"

# Method1: first occurence of every character in the string
#
occ_dict={}
enum_string = enumerate(mystring)
print(list(enum_string)) ###[(0, 'a'), (1, 'g'), (2, 'g'), (3, 'r'), (4, 'e'), (5, 'g'), (6, 'a'), (7, 't'), (8, 'o'), (9, 'r')]

for i, c in enum_string:
    if c not in occ_dict:
        occ_dict[c]=i

print(occ_dict)

##Method2 without using enum

occ_dict={}
index=0

for c in mystring:
    if c not in occ_dict:
        occ_dict[c]=index
    index+=1

print(occ_dict)