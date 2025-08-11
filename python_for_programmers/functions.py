def add_three(num1, num2, num3):
    sum_three = num1 + num2 + num3
    return sum_three

sum_output = add_three(2, 4, 6)
print(sum_output)

def greeting(language):
    if language == 'Spanish':
        greeting = 'Hola'
    elif language == 'English':
        greeting = 'Hello'
    elif language == 'French':
        greeting = 'Bonjour'

    print(greeting)

greeting('French')