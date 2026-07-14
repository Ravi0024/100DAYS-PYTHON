#for loops in python
'''loops in python:sometimes we need to execute a block of code several times. 
                    In python we have for loops , while loops and nested loops to do that.'''
"""for loops:for loops are used to iterate over a sequence of iterable objects in pyton
Iterate over a list,tuple, string, dictionary, dictionaries, set or range of numbers"""
#iterating over a string

name="RAVI TEJA"
for i in name:
    print(i , end=",")

#iterating over a list  
fruits=["apple","banana","orange"]
for x in fruits:
    print(x)
    for y in x:
        print(y , end=" ")

#range()-if we want to use a for loop for a specific number of times, we can use the range() function to generate a sequence of numbers.
for i in range(5):
    print(i)

for i in range(1, 10, 2):#it prints the numbers from 1 to 9 with a step of 2
    print(i)