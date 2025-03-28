dict1 ={
"a":5,
    "d":2,
    "b":7,
    "z":8
}

res = {k:i for k,i in dict1.items() if k=="a"}

print(res)

