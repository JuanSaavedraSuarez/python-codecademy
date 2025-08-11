class Animal:
    def eat(self):
        print("Nom nom nom")

class Dog(Animal):
    def bark(self):
        print("bark")

class Cat(Animal):
    def meow(self):
        print("meow")

fluffy = Dog()
zoomie = Cat()

fluffy.eat()
zoomie.eat()

####################################################################################################

class Employee():
    new_id = 1
    
    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1

    def say_id(self):
        print("My id is {}.".format(self.id))

class Admin(Employee):
    pass

e1 = Employee()
e2 = Employee()
e3 = Admin()

e3.say_id()