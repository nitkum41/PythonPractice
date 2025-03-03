mylist=[1,2,3,5,3,6,7,9,3,10,11,1]

res=[]

##m1
for val in mylist:
    if val not in res:
        res.append(val)


print("final list",res)
# print("duplicate elements",dup)

##m2
print(list(set(mylist)))