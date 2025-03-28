class A:
    def __init__(self):
        print("inside A constructor")

    def func(self):
        print("inside A")


class B(A):
    def __init__(self):
        print("inside B constructor")

    def func(self):
        print("inside B")


class C(B):
    def __init__(self):
        super(C,self).func()
        # super().func() ## call func() of B


# print(C.__mro__)

obj = C()
