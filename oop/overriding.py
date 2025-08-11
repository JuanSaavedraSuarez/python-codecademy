class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_noise(self):
        print("{} says, Grr".format(self.name))

pet1 = Animal("Rex")
pet1.make_noise()

class Cat(Animal):
    def make_noise(self):
        print("{} says, Meow!".format(self.name))

pet2 = Cat("Maisy")
pet2.make_noise()

##################################################################################################

class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class Admin(Employee):
  # Write your code below
  def say_id(self):
    print("I am an Admin")

e1 = Employee()
e2 = Employee()
e3 = Admin()
e3.say_id()
