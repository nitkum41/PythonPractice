import copy


##there won't be any difference between a shallow copy and a deep copy.
# The difference appears when the source contains properties that are collections or complex objects. Consider the following:

## shallow copy
a=[[1,2],[3,4]]

c = copy.copy(a)

a[0][1]=10


print(a,c)



## deep copy

b=[[1,2],[3,4]]

d = copy.deepcopy(b)

d[0][0]=10

print(b,d)

