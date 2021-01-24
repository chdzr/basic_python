class MyClass:
    x = 5

class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def myfunc(self):
        print("Hello my name is " + self.name)

person1 = Person("John",36)
print(person1.name)
person1.myfunc()


my_class = MyClass()
print(my_class.x)