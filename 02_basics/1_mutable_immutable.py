# Mutable and Immutable Data Types in Python
# Mutable or immutable is the fancy word for explaining the property of data types of being able to get updated after being initialized. The basic explanation is thus: A mutable object is one whose internal state is changeable. On the contrary, once an immutable object in Python has been created, we cannot change it in any way.

# What are Mutable Data Types?
# Anything is said to be mutable when anything can be modified or changed. The term "mutable" in Python refers to an object's capacity to modify its values. These are frequently the things that hold a data collection.

# What are Immutable Data Types?
# Immutable refers to a state in which no change can occur over time. A Python object is referred to as immutable if we cannot change its value over time. The value of these Python objects is fixed once they are made.

# List of Mutable and Immutable objects
# Python mutable data types:


# Lists
# Dictionaries
# Sets
# User-Defined Classes (It depends on the user to define the characteristics of the classes)
# Python immutable data types:

# Numbers (Integer, Float, Complex, Decimal, Rational & Booleans)
# Tuples
# Strings
# Frozen Sets

username = "aliakbar"

print(username)

username = "ali"

print(username)

x = 10
y = x

print(x)

print(y)

x = 15

print(y)

# mutable and immutable is about changing of that specific value in memory

# Mutable Objects:
# Mutable objects are those whose internal state can be changed after creation.

# my_set = {1, 2, 3}
# my_set.add(4) # Modifies the set by adding a new element
# print(my_set) # Output: {1, 2, 3, 4}
# # Removing an element from the set
# my_set.remove(3)
# print(my_set) # Output: {1, 2, 4}

# Immutable Objects:
# Integer: Integers are immutable objects in Python. When you modify an integer, a new object is created instead of modifying the existing one.
#  x = 10
#  y = x # y points to the same integer object as x
#  y += 5 # A new integer object is created with the value 15 and y points to it
#  print(x) # Output: 10 (x remains unchanged)
#  print(y) # Output: 15 (new object created)