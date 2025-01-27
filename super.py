class A:
    def __init__(self):
        pass

    def func(self):
        print("inside A")


class B(A):
    def __init__(self):
        pass

    def func(self):
        print("inside B")


class C(B):
    def __init__(self):
        super(B, self).func()


# print(C.__mro__)

obj = C()
