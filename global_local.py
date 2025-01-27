###list

# l=[1,2,3,4]
# print(l[:])  #all
# print(l[:-1]) #skip last
#
# print(l[-1:])  #last element
#


gl = list()


def f1():
    global gl  ##use global keyword to use global inside a function
    gl.append(1)


def f2():
    print(gl)


print(gl)
f1()
f2()
