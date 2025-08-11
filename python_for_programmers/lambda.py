# aka anonymous functions, are small, inline functions that can have any number of
# arguments but only one expression. They are defined using the lambda keyword and are
# typically used for short, simple, operations.

# regular function
def square(x):
    return x ** 2

# lambda function
square_lambda = lambda x: x ** 2
add_lmabda = lambda a,b: a + b
print(add_lmabda(3, 5))

# syntax of lambda function:
# lambda [args]: [expression]

greeting = lambda name: f"Hello, {name}"

print(greeting("Alice"))

# map() applies given lambda to each item in a list
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squred)

# filter() creates a new list of elemtns for whic the given lambda function returns True
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# sorted can use lambda as a key for custom sorting
students = [('Alice', 'A', 15), ('Bob', 'B', 12), ('Charlie', 'A', 20)] 
# sorts based on the third element of the tuple, age
sorted_students = sorted(students, key = lambda x: x[2])

print(sorted_students)

# lambda advantages:
#   concise and easy to read
#   convenient for throwaway functions, especially as argumetns to higher order functions
# lambda disadvantages:
#   can only contain expressions not statements
#   limited to single expression, which can make complex operations difficult
#   they can be harder to debug due to their anonymous nature

