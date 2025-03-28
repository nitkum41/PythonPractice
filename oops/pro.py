class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def _display(self):
        print("Name:", self._name)
        print("Age:", self._age)


class Student(Person):
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self._roll_number = roll_number

    def display(self):
        self._display() ## protected method accessed from derived class
        print("Roll Number:", self._roll_number)


s = Student("John", 20, 123)
s.display()