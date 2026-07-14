""" set methods in python -  Some of the commonly used set methods are: union(), update(), intersection(), intersection_update(),
                          symmetric_difference(), symmetric_difference_update(), difference(), difference_update() etc.   """
# 1. union() - returns a set containing all items from both sets, duplicates are removed

city1 = {"delhi","mumbai","kolkata"}
city2 = {"chennai","bangalore","delhi"}
city = city1.union(city2)
print(city)

# 2. update() - adds items from another set to the current set
city1.update(city2)
print(city1 )

# 3. intersection() - returns a set containing only items that are present in both sets
city3 = city1.intersection(city2)
print(city3)

# 4. intersection_update() - removes items from the current set that are not present in another set
city1.intersection_update(city2)
print(city1)

# 5. symmetric_difference() - returns a set containing items that are in either set, but not in both
n1 = {1,2,3,4,5}
n2 = {4,5,6,7,8}
n = n1.symmetric_difference(n2)
print(n)

# 6. symmetric_difference_update() - updates the current set with items that are in either set, but not in both
n1.symmetric_difference_update(n2)
print(n1)

# 7. difference() - returns a set containing items that are in the current set but not in another set
d1 = {"a", "b", "c", "d", "e"}
d2 = {"c", "d", "e", "f", "g"}
d = d1.difference(d2)
print(d)

d= d2.difference(d1)
print(d)

# 8. difference_update() - removes items from the current set that are present in another set
d1.difference_update(d2)    

"""   set methods   - there are several built in methods used for the manipulation of sets in python.   """
#isdisjoint() - returns True if two sets have a null intersection means no common elements, otherwise it returns False
s1 = {1,2,3}    
s2 = {4,5,3,6}
print(s1,s2)
print(s1.isdisjoint(s2))
#issuperset() - returns True if the current set contains all items of the specified set, otherwise it returns False
s1 = {1,2,3,4,5}    
s2 = {1,2,3}
print(s1.issuperset(s2))
#issubset() - returns True if all items of the specified set are present in the current set, otherwise it returns False
s1 = {1,2,3}
s2 = {1,2,3,4,5}
print(s1.issubset(s2))
#add() - adds an item to the current set, if the item is already present, it does not add any item
s1 = {1,2,3}
s1.add(4)
print(s1)
#update() - adds items from another set to the current set, if the item is already present, it does not add any item
s1.update({5,6,7})
print(s1)
#remove() - removes the specified item from the current set, if the item is not present, it raises a KeyError
s1.remove(2)
print(s1)
#discard() - removes the specified item from the current set, if the item is not present, it does not raise any error
s1.discard(3)
print(s1)
#pop() - removes and returns an arbitrary item from the current set, if the set is empty, it raises a KeyError
#s1.pop()
#print(s1)
#del() - deletes the current set, if the set is not present, it raises a NameError
del s1
#print(s1)
#clear() - removes all items from the current set, the set will be empty after this operation
c1 = {1,2,3}
c1.clear()
print(c1)

#check if item exist
s1 = {1,2,3,4,5}
if 3 in s1:
    print("3 is present in the set")
else:
    print("3 is not present in the set")