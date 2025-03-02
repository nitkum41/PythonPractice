mystring="aggregator"

# Method1: first occurence of every character in the string
#
# occ_dict={}
# enum_string = enumerate(mystring)
#
# for i, c in enum_string:
#     if c not in occ_dict:
#         occ_dict[c]=i
#
# print(occ_dict)

##Method2 without using enum

occ_dict={}
index=0

for c in mystring:
    if c not in occ_dict:
        occ_dict[c]=index
    index+=1

print(occ_dict)