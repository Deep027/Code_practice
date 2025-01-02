a = [10, 20, 15]
print(a)

# Creating a List 
# Here are some common methods to create a list: 
# Using Square Brackets

# List of integers
a = [1, 2, 3, 4, 5]

# List of strings
b = ['apple', 'banana', 'cherry']

# Mixed data types
c = [1, 'hello', 3.14, True]

print(a)
print(b)
print(c)

# Using list() Constructor
# We can also create a list by passing an iterable 
# (like a string, tuple, or another list) to list() function.

# From a tuple
a = list((1, 2, 3, 'apple', 4.5))  

print(a)

# Creating List with Repeated Elements
# Create a list [2, 2, 2, 2, 2]
a = [2] * 5

# Create a list [0, 0, 0, 0, 0, 0, 0]
b = [0] * 7

print(a)
print(b)

# Accessing List Elements
# Elements in a list can be accessed using indexing. 
# Python indexes start at 0, so a[0] will access the first element, while negative indexing allows us to access elements from the end of the list. 
# Like index -1 represents the last elements of list.

a = [10, 20, 30, 40, 50]

# Access first element
print(a[0])    

# Access last element
print(a[-1])

# Adding Elements into List
# We can add elements to a list using the following methods:

# append(): Adds an element at the end of the list.
# extend(): Adds multiple elements to the end of the list.
# insert(): Adds an element at a specific position.

# Initialize an empty list
a = []

# Adding 10 to end of list
a.append(10)  
print("After append(10):", a)  

# Inserting 5 at index 0
a.insert(0, 5)
print("After insert(0, 5):", a) 

# Adding multiple elements  [15, 20, 25] at the end
a.extend([15, 20, 25])  
print("After extend([15, 20, 25]):", a)

# Updating Elements into List
# We can change the value of an element by accessing it using its index.

a = [10, 20, 30, 40, 50]

# Change the second element
a[1] = 25 

print(a)