mystring ="we@3&*(1234lcom56e"

res=""
for i in mystring:
    if i.isalpha():
        res+=i

print(res)