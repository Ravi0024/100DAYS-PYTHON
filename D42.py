"   ENUMERATE FUNCTION    "
"""
The enumerate() function in Python is a built-in function that allows you to loop over 
sequence (like a list, tuple, or string) and get the index and value of each item in the
sequence at the same time. It returns an enumerate object, which can be converted into a list or tuple if needed.
"""

print("   example on lists    ")
fruits = ['apple', 'banana', 'cherry', 'date']
# Using enumerate() to get index and value
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

"""
as you can see, the enumerate() function returns a tuple containing the index and value of each element in the sequence.
you can use the for loop to unpack these tuples and assign them to variables,as shown in the example above.
"""

"   changing the starting index    "
"""

by default, the enumerate() function starts counting from 0, but you can specify a different starting index
by passing it is an argument to the enumerate function.

"""

print("   example on lists with starting index of 1    ")
#loop over a little and print the index (starting at 1) and value of each element
fruits = ['apple', 'banana', 'cherry', 'date']
# Using enumerate() with a starting index of 1
for index, fruit in enumerate(fruits, start=1):
    print(f"Index: {index}, Fruit: {fruit}")

"""
the enumerate function is often used when you need to loop over a sequence and perform some aciton with both the index and value pf each element.
for example you might use it to loop over a list of strings and print the index and value of each string in a formatted way:

"""

print("   example on lists with upper case letters    ")
fruits  = ['apple', 'banana', 'cherry', 'date']
for index,fruit in enumerate(fruits):
    print(f"{index}: {fruit.upper()}")

"""in addition to lists , you can use the enumerate function with any other sequence type in python , 
such as tuples and strings .
here's an example with a tuple:
"""
print("example on tuples")
#loop over a tuple and print the index and value of each element
colors = ('red', 'green', 'blue', 'yellow')
for index,color in enumerate(colors):
    print(f"Index: {index}, Color: {color}")

"     example on strings     "
print("example on strings")
#loop over a string and print the index and value of each character
word = "hello"
for index, c in enumerate(word):
    print(f"Index: {index}, Character: {c}")