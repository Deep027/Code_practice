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

# Removing Elements from List
# We can remove elements from a list using:

# remove(): Removes the first occurrence of an element.
# pop(): Removes the element at a specific index or the last element if no index is specified.
# del statement: Deletes an element at a specified index.

a = [10, 20, 30, 40, 50]

# Removes the first occurrence of 30
a.remove(30)  
print("After remove(30):", a)

# Removes the element at index 1 (20)
popped_val = a.pop(1)  
print("Popped element:", popped_val)
print("After pop(1):", a) 

# Deletes the first element (10)
del a[0]  
print("After del a[0]:", a)

# Using len()
# Using Max()

a = [1, 2, 3, 4, 5]
length = len(a)
print(length)

a = [10, 24, 76, 23, 12]

# Max() will return the largest in 'a'
largest = max(a)
print(largest)

a = [10, 20, 30, 40, 50]

# Swapping elements at index 0 and 4
# using multiple assignment
a[0], a[4] = a[4], a[0]

print(a)

a = [10, 20, 30, 40, 50]

# Check if 30 exists in the list
if 30 in a:
    print("Element exists in the list")
else:
    print("Element does not exist")

# list of animals
Animals= ["cat", "dog", "tiger"]
# searching positiion of dog
print(Animals.index("dog"))

a = [1, 2, 3, 4, 5]

# Reverse the list in-place
a.reverse()
print(a)

a = [1, 2, 3]
b = [4, 5, 6]

# Merge the two lists and assign
# the result to a new list
c = a + b
print(c)

# List Methods
# Let’s look at different list methods in Python:

# append(): Adds an element to the end of the list.
# copy(): Returns a shallow copy of the list.
# clear(): Removes all elements from the list.
# count(): Returns the number of times a specified element appears in the list.
# extend(): Adds elements from another list to the end of the current list.
# index(): Returns the index of the first occurrence of a specified element.
# insert(): Inserts an element at a specified position.
# pop(): Removes and returns the element at the specified position (or the last element if no index is specified).
# remove(): Removes the first occurrence of a specified element.
# reverse(): Reverses the order of the elements in the list.
# sort(): Sorts the list in ascending order (by default).

# list slicing:
# list_name[start : end : step]

# list comprehension
# [expression for item in iterable if condition]

