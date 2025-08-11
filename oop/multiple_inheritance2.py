class Animal:
    def __init__(self, name):
        self.name = name
    
class Dog(Animal):
    def action(self):
        print("{} wags tail. Aww".format(self.name))

class Wolf(Animal):
    def action(self):
        print("{} bits. OUCH".format(self.name))

class Hybrid(Dog, Wolf):
    def action(self):
        super().action() # invokes Dog action since Dog is listed first
        Wolf.action(self)

my_pet = Hybrid("Fluffy")
my_pet.action()

##############################################################################################

class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class User:
  def __init__(self, username, role="Customer"):
    self.username = username
    self.role = role

  def say_user_info(self):
    print("My username is {}".format(self.username))
    print("My role is {}".format(self.role))

# Write your code below
class Admin(Employee, User):
  def __init__(self):
    super().__init__()
    User.__init__(self,self.id, "Admin")
    

  def say_id(self):
    super().say_id()
    print("I am an admin.")

e1 = Employee()
e2 = Employee()
e3 = Admin()
e3.say_user_info()