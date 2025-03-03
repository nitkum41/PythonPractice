## swap first and last element of list using temp var

list1=[1,2,3,4,5]
#
# a=list1[0]
#
# list1[0]=list1[-1]
#
# list1[-1]=a
#
#
# print(list1)

### using tuple


# list1[0],list1[-1]=list1[-1],list1[0]
# print(list1)

### using * best

start,*all,end = list1

list1 = [end,*all,start]
print(list1)


##using pop insert append

a=list1.pop(0)
b=list1.pop(-1)
list1.insert(0,b)
list1.append(a)

print(list1)

