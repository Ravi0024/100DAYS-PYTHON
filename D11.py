#Strings in python
"""anything enclosed in single or double quotes is a string.
Strings are immutable, which means that once a string is created, it cannot be modified.
Strings can be concatenated using the + operator, and repeated using the * operator.
Strings can be indexed and sliced using square brackets [].
Strings have many built-in methods for manipulating and formatting them, such as upper(), lower(), strip(), split(), join(), etc.
String literals can be enclosed in single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).
Triple quotes are used for multi-line strings or docstrings."""
#Examples of strings in python
#Using single quotes
string1 = 'Hello, World!'
print(string1)  # Output: Hello, World!
#Using double quotes
string2 = "Python is great!"
print(string2)  # Output: Python is great!
#Using triple quotes for multi-line string
string3 = '''This is a multi-line string.
It can span multiple lines.'''
print(string3)
# Output:
# This is a multi-line string.
# It can span multiple lines.

#Concatenating strings
string4 = string1 + " " + string2
print(string4)  # Output: Hello, World! Python is great!

name='Ravi'
greeting = "Hello, " + name + "!"
print(greeting)  # Output: Hello, Ravi!

#Accessing characters in a string
'''In python , strings are like arrays of characters, and you can access individual characters using their index.
The index of the first character is 0, the second character is 1, and so on.
 You can also use negative indexing to access characters from the end of the string, where -1 is the last character, 
 -2 is the second to last character, and so on.
 square brackets [] are used to access characters in a string.'''
first_char = name[0]
print(first_char)  # Output: R

#Looping through a string
'''we can use a for loop through each character in a string.'''
for char in name:
    print(char)  # Output: R, a, v, i