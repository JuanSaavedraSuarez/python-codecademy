class Animal:
    def __init__(self, name, sound='Grrrr'):
        self.name = name
        self.sound = sound

    def make_noise(self):
        print("{} says, {}".format(self.name, self.sound))

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Meow!")

pet_cat = Cat("Rachel")
pet_cat.make_noise()

#################################################################################################

class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class Admin(Employee):
  def say_id(self):
    # Write your code below:
    super().say_id()
    print("I am an admin.")

e1 = Employee()
e2 = Employee()
e3 = Admin()
e3.say_id()