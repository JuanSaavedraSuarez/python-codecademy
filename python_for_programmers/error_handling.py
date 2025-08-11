# try attempts to execute block
# except executes another block if try fails

nums = [0, 1, 2, 3]

try:
    print(sum(nums))
except:
    print('Cannot print the sum! Variable is not numbers')

nums0 = ['x', 'y', 'z']

# finally executes block regardles of clause

try:
    print(sum(nums0))
except:
    print('Cannot print the sum! Variable is not numbers')
finally:
    print('Hope you get the result you want!')
