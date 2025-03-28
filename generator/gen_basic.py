def func(n):
    yield 2**n


for i in range(10):
    f=func(i)
    # print(next(f))
    # print(next(func(i)))
  