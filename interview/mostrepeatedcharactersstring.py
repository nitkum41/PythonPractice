mystring="aggregator"

my_dict={}
for i in mystring:
    if i in my_dict:
        my_dict[i]+=1
    else:
        my_dict[i]=1

char=""
count=0

for c,i in my_dict.items():
    if i>count:
        count=i
        char=c

print(char)

