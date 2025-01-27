# class A:
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
#
#     def func(self, name):
#         self.name = name
#
#     def func(self, name, age):
#         self.name = name
#         self.age = age
#
#     def func(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
#         print(f'{name} is {age} years old and lives in {address}')
#
#
# obj = A('Nitesh', 28, 'marathalii')
# obj.func('N',23,'xyx')
#
class A:
    def __init__(self, age):
        self.age = age

    def func(self, name):
        print('name inside class a  is :', name)


class B(A):
    def __init__(self):
        super().func("bh")  ##super invokes constructor of parent class

    def func(self, name):
        print('name inside class b is : ', name)


obj = A("12")
obj.func('Nitesh')
# obj = B()
# obj.func('Nitesh')
