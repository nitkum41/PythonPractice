#default argument

def func(a="first",b="second"):
    print(a,b)


func("third","fourth")


## tuple has to be first then followed by dictionary in variable positioning

def func1(*data,**data1):
    print(type(data1),len(data1))
    print(type(data),data)


func1(7,8,9,a="one", b="two", c="three")