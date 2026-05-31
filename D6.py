'''variable 

it is like a container that holds a value. 
It can be used to store and manipulate data in a program.
Variables can be assigned different types of values, such as numbers, strings, or lists.
They can also be updated or changed throughout the program as needed.
In Python, you can create a variable by simply assigning a value to it using the equals sign (=).
For example:age = 25
name = "John"   
a=true
In this example, we have created three variables: "age" which holds the value 25,
"name" which holds the string "John", and "a" which holds the boolean value true.'''


"""DATATYPES
    It specifies the type of data that a variable can hold.
    This is required in programming to do various operations without errors
In Python, there are several built-in data types, including:
1. Numeric Types: int (integer), float (floating-point number), complex (complex number)
2. Text Type: str (string)
3. Boolean Type: bool (boolean)
4. Sequence Types: list, tuple, range
5. Mapping Type: dict (dictionary)
6. Set Types: set, frozenset   
"""
int=1,-4,0,3,100
float=3.14,-0.5,0.0,2.71828
complex=2+3j, -1-4j, 0+0j

str="Hello, World!", "Python is great!", "Data types in Python"

bool=True, False

'''"A list is a collection of items that are ordered and changeable. Lists are defined by enclosing the items in square brackets[] [] and separating them with commas. 
Lists can contain items of different data types, including numbers, strings, and even other lists.
You can access individual items in a list using their index, which starts at 0.'''

list=[1, 2, 3, 4, 5], ["apple", "banana", "cherry"], [1, "hello", True]

'''A tuple is a collection of items that are ordered and unchangeable. Tuples are defined by enclosing the items in parentheses () and separating them with commas.
You can access individual items in a tuple using their index, which starts at 0.'''

tuple=(1, 2, 3, 4, 5), ("apple", "banana", "cherry"), (1, "hello", True)

'''Dictionaries are collections of key-value pairs that are unordered, changeable, and indexed. 
They are defined by enclosing the items in curly braces {} and separating them with commas.
 Each key is separated from its value by a colon (:).'''

dict={"name": "Ravi", "age": 21, "city": "Vijayawada", "male": True}

print(int)
print(float)
print(complex)
print(str)
print(bool)
print(list)
print(tuple)
print(dict)
print(list[0])  # Accessing the first item in the list
print(tuple[1])  # Accessing the second item in the tuple
print(dict["name"])  # Accessing the value associated with the key "name" in the dictionary

