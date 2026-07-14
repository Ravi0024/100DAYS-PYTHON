#introduction to lists in python
"""Lists are ordered collection of data items.
lists are mutable data types means can be altered
separated by commas and enclosed within the square brackets[]
stores multiple values in single variable
example:      """
lst1=["apple","banana","cucumber"]
lst2=["R","A","V","I"]
print(lst1)

#list indexing : we can access the items in the list using the indexing number in the list
# 1.positive indexing   
print(lst2[3])

#2.negative indexing
print(lst1[-1])


'we can find the length of the list using len() '
print(len(lst1))

print(lst1[2:-1])


#to check weather an item in the list we using the ' in ' keyword
color=["black","white","red","blue","green"]
print(color)
if "brown" in color:
    print("selected color is their")    
else:
    print("Nooooo")


#Range of index
'syntax: listname[ start : end : jumpindex ]'
print(color[0:3])


"""list comprehension - used to create a new list from other iterables likke tuples,lists,dictionaries,sets and even in arrays and strings
syntax:
List = [Expression(item) for item in iterable if condition]  
Expression : it is the  item which is being iterated
Iterable : it can be lists , tuples,dictionaries,sets, and even in arrays and strings
condition : checks if the item should be addes to the new list or not

ex:accepts items with the small letter '0' in the new list """
names =["ravi","teja","pra","pavi","che"]
namesWith_t = [item for item in names if "t" in item]
print(namesWith_t)

#squares
lst = [i*i for i in range(4)]
print(lst)
#even
lste = [i*i for i in range(6) if i%2==0]
print(lste)