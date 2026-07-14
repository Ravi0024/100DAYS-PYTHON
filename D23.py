#list methods in python
"list.sort() - sports the list in ascending order"
colors=["violet","green","bluue","indigo"]
colors.sort()
print(colors)

"reverse() - it reverse the list"
colors.reverse()
print(colors)

"index() - returns the index of the first occurence of the list"
print(colors.index("green"))

"count() - counts the no of items in the list"
num=[1,2,3,3,4,2,6,7]
print(num.count(2))

"copy() - returns the copy of the list"
newlst=colors.copy()
print(newlst)

"append() - this method adds the item to the end of the existing list"
colors.append("purple")
print(colors)

"insert() - this method inserts the value at the given index"
colors.insert(0,"orange")

"extend() - this method extends the entire list with another new list"
print(colors)
rainbow = ["v","i","b","g","y","o","r"]
colors.extend(rainbow)
print(colors)

"concatenating 2 lists - we can join 2 lists using '+' symbol"
list1=["a","b","c"]
list2=[1,2,3,4]
print(list1+list2)