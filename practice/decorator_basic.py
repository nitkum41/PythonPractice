def add(f1):
    print("inside add")
    return f1


@add
def func():
    print("inside func")
    return "func"


res = func()
print(res)


##output
# inside add
# inside func
# func