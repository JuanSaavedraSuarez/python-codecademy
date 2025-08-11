def factorial(num):
    call_stack = []
    if num == 1: # base case
        print("Base case: Num is 1")
        return 1
    else: # recursive step
        call_stack.append({'input': num})
        print('call stack: ', call_stack)
        return num * factorial(num - 1)

num = int(input("Factorial?\n"))

print(factorial(num))
