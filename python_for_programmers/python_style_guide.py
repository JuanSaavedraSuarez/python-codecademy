####################################################################################################

# Class names use CapWords
class MyDog:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("My dog's name is: ", self.name)

x = MyDog('Pepper')

####################################################################################################

# Function names use snake_case
def calculate_force(mass, acc):
    force = mass * acc
    return force
#### Note the four spaces per indentation

####################################################################################################

# Execute script:
# python3 myscript.py

def main():
    print('Hello World!')

if __name__ == '__main__':
    main()

def main():
  print('This line is printed directly from the main function of the program')
  secondary_function()

def secondary_function():
  print('This line is printed from a secondary function call within the main function')

if __name__ == '__main__':
  main()
