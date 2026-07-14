"Operations on tuples in python"

# Manipulating Tuples - tuples are immutable.to change ,add or remove items in the tuple we have to convert it into list.after changing convert into tuple
countries = ("ind","ussr","italy","france","england")
temp = list(countries)    #converting tuple into list
print(temp)

#appending item 
temp.append("usa")
print(temp)

#removing an item
temp.pop(5)
print(temp)

#changing item
temp[4]="britan"
print(temp)

#converting list into tuple
countries = tuple(temp)
print(countries)

"concatenating tuples using '+' symbol"
print(countries)
countries2=("pak","bangl","nep")
print(countries2)
print(countries+countries2)

#tuple metods
'count() - returns no of times the given item appeared in the tuple'
c = countries2.count('bangl')
print(c)

'index() - returns the first occurance of the given element from the tuple'
#syntax = tuple.index(element, start, end)
tuple = (0,1,2,3,4,5,6)
res = tuple.index(2)
print(res)

