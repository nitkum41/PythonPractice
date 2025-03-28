

def func():
    x=0
    y=1
    while True:
        yield x
        x,y = y,x+y

n = int(input("How many values of fibonacci series"))
f=func()
# print(next(f))

for i in range(n):
    print(next(f))

# a = 8 #raw_input
#
# def fib_gen():
#     a, b = 0, 1
#     while 1:
#         yield a
#         a, b = b, a + b
#
# fs = fib_gen()
# next(fs)
# for i in range(a):
#     print(next(fs))