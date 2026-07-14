#tuples in python
"""tuples are ordered collection of data items.they store multiple values in a single variable.
items in the tuples are separated by commas,enclosed by circular brackets().
TUPLES are IMMUTABLE means unchangeable after creation """

tuple1=(1,2,3,4,5)
tuple2=("a","b","c")
# print(tuple1,tuple2)


#tuple indexing - index no is used to access any particular item in the tuple
index=("ind","pak","ban")
print(index)
''' 
    1. Positive indexing - like [0], [1],... 
'''
print(index[1])
'''
    2. Negative indexing - used to access iems from end of the list like [-1], [-2],... 
'''
print(index[-3])
'''
    3. Check for item - used to check the item in tuple using 'in' keyword
'''
index=("ind","pak","ban")
if "nep" in index:
    print("present")
else:
    print("noob")

'''
    4. Range of index - we can print a range of tuple items by specifying where do you  want to start,
       where do you want to end and if you want to skip elements in between range.
       syntax : Tuple[ start : end : jumpIndex ]
'''
#printing a tuple within a particular range
animals=("ape","buffalo","cow","donkey","elephant","fox")
print(animals[0:4])
print(animals[-1:0])
