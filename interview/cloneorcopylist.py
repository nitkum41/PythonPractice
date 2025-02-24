
list1=[1,2,3,4,5]

###########################
list2=list1.copy()

print(list2)

################################
list3=list1[:]
print(list3)


##########################
list4=[]

list4.extend(list1)
print(list4)



##############################

list5 = list(list1)
print(list5)

############################
list6 = [i for i in list1 ]

print(list6)
