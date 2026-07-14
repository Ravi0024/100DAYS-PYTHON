"""TYPE CASTING - converting one data type to another"""
'''Python supports a wide range of data types, and sometimes you may need to convert one data type to another. 
This process is called type casting. Python provides built-in functions for type casting, such as
 int(), float(), str(), ord(),hex(),oct(),tuple(),set(),list(),dict() and bool().'''
#2 types of type casting

#1. Implicit type casting (automatic) - Python automatically converts one data type to another when necessary.
#Example:
x = 5   # integer
y = 3.14  # float
result = x + y  # x is implicitly converted to float
print(result)  # Output: 8.14   


#2. Explicit type casting (manual) - You can manually convert a data type using built-in functions.
#Example:   
a = 10  # integer
b = float(a)  # explicitly converting integer to float
print(b)  # Output: 10.0
c = "123"  # string 
d = int(c)  # explicitly converting string to integer
print(d)  # Output: 123
e = 3.14  # float
f = str(e)  # explicitly converting float to string
print(f)  # Output: '3.14'
g = 1  # integer
h = bool(g)  # explicitly converting integer to boolean
print(h)  # Output: True
i = 0  # integer
j = bool(i)  # explicitly converting integer to boolean
print(j)  # Output: False
#Note: When performing type casting, be cautious of potential data loss or errors. 
'''For example, converting a float to an integer will truncate the decimal part, 
and converting a non-numeric string to an integer will raise a ValueError.
 Always ensure that the data you are trying to convert is compatible with the target data type.'''
