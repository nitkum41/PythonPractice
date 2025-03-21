""""
what is POJO ?

what is result set ?

pipelines linking in project ?

how to handle data in json and modify it for different scenarios ?


pandas - json to excel ?

DB testing
"""
### get unique and du[licates from list
name = "AabkKQ"

######method 1 using list #####################
name1=name.lower()
res=[]
output=[]
for i in range(0,len(name1)):
    if name1[i] in name1[i+1:]:
        res.append(name1[i])

for i in name1:
    if i not in res:
        output.append(i)
print(res,output)

#####################method 2 using dic#########
my_dict={}
for char in name1:
    if char in my_dict:
        my_dict[char]+=1
    else:
        my_dict[char]=1

print(my_dict)

for k,v in my_dict.items():
    if v==1:
        print("non repeated value",k)
    if v>1:
        print("repeated char",k)



