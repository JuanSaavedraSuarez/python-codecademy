####################################################################################################
# lists
# ordered collections of items, can contain different data types, resizable array

lst = ['abc', 123, 'def', 10.5, 62, ['g', 'h', 'i']]

# list items can be accessed with its index
print(lst[0])
print(lst[4:6])

print(len(lst))

# append item to end of list
lst.append(99)

# remove item passed as arg
lst.remove(62)

# pop removes and returns item at specified index
# if no index, takes last item
lst.pop() # removes ['g', 'h', 'i']
lst.pop(0) # removes 'abc'

####################################################################################################
# tuples
# more memory efficient than lists
# slightly higher time efficiency than lists
# immutable unlike lists
my_tuple = ('abc', 123, 'def', 456, 789, 'ghi')

# can hold single item
ex_tuple = ('abc', )

print(my_tuple[0])
print(my_tuple[3:5])

print(len(my_tuple))

# max returns maximum value assuming all values are either numbers or strings
int_tuple = (65, 2, 88, 101, 25)
max(int_tuple) # returns 101

str_tuple = ('orange', 'blue', 'red', 'green')
max(str_tuple) # returns "red"
 
mix_tuple = ('abc', 234, 567, 'def')
# max(mix_tuple) # throws an error!

# min returns the minimum values, similar to max
min(int_tuple)
min(str_tuple)
# min(mix_tuple)

# index returns index value for argument
my_tuple.index('abc')
my_tuple.index(456)

# count returns number of occurrences of arg in tuple
my_tuple.count('abc')

####################################################################################################
# dictionaries
# defined with brackets, contain key-value pairs, referring to pairs of key and value separated 
# by a colon :
# can hold different data types, including lists and nested dictionaries. However keys must be 
# immutable like strings, numbers or tuples

groceries = {'fruits': ['mangoes', 'bananas', 'kiwis'],
            'protein': ['beef', 'pork', 'salmon'],
            'carbs': ['rice', 'pasta', 'bread'],
            'veggies': ['lettuce', 'cabbage', 'onions']}

# values can only be accessed and updated using its key
party_planning = {'Yes': 10,
                  'No': 15,
                  'Maybe': 30,
                  'Location': 'Our Backyard',
                  'Date': '2022/05/01'}
 
party_planning['Location'] # returns 'Our Backyard'
party_planning['Location'] = 'At the park'
party_planning['Location'] # prints 'At the park'
party_planning['Dress Code'] = 'Casual'

len(party_planning)

# update takes a dictionary as an argument to update an existing dictionary
# any new values are added to the exiting dictionary and overlapping key-value pairs are 
# overwrittent by the new values

shopping_list1 = {'jewelry': 'earrings', 'clothes': 'jeans', 'budget': 200}
shopping_list2 = {'shoes': 'sandals', 'budget': 350}
 
shopping_list1.update(shopping_list2)
 
print(shopping_list1) # prints {'jewelry': 'earrings', 'clothes': 'jeans', 'budget': 350, 'shoes': 'sandals'}

# keys and values can be used to return keys and values from a dictionary
shopping_list = {'jewelry': 'earrings', 'clothes': 'jeans', 'budget': 200}
 
shopping_list.keys() # returns dict_keys(['jewelry', 'clothes', 'budget'])

shopping_list.values() # returns dict_values(['earrings', 'jeans', 200])

####################################################################################################
# sets
# sets are immutable unordered collection of unique elemetns that consist of ints, floats, strs, 
# and tuples. Cannot hold mutalbe elements like lists or dictionaries
set1 = {'Jenny', 26, 'Parker', 10.5}
print(set1) # prints {10.5, 26, 'Jenny', 'Parker'}

# sets do not have indexes or keys, use in to check if value exists in set
students = {'Jane', 'Carlos', 'Amy', 'Bridgette', 'Chau', 'Dmitry'}
print('Chau' in students) # returns True

# sets are immutable, so elements within cannot be changed, but new elements can be added using add
# if an element already exists in set it wont be added
students.add('George')
print('George' in students)

# update takes any iterable object, and adds it to existing set, any duplicate elements will not be added
students1 = {'Jane', 'Carlos', 'Amy', 'Bridgette', 'Chau', 'Dmitry'}
students2 = {'Alice', 'Lily', 'Zhuo', 'Amy', 'Jane'}
 
students1.update(students2)

# union takes iterable object and joins the new object with existing object
students3 = students1.union(students2)

# remove takes in an element and removes it from set

students = {'Jane', 'Carlos', 'Amy', 'Bridgette', 'Chau', 'Dmitry'}
students.remove('Bridgette')

# for loops
count_down = set([9, 8, 7, 6, 5, 4, 3, 2, 1])
for num in count_down:
    print(num, 'seconds left!')