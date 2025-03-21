mystring="aggregator"

my_dict={}
for i in mystring:
    if i in my_dict:
        my_dict[i]+=1
    else:
        my_dict[i]=1

print(my_dict)
char=""
count=0

##getting largest count from the values section

for c,i in my_dict.items():
    if i>count:
        count=i
        char=c

print(char)

