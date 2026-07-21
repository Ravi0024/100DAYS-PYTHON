"   DICTIONARIES METHODS IN PYTHON -Several built-in methods used to manipulate dictionaris  "
#updtae() - used to update the value of the key provided to it in the item already exists in the dictionary. if the key does not exist, it will create a new key-value pair.
info = {'name' : 'Ravi','age' : '21','eligible' : True}
print(info)
info.update({'age' : '22'})
print(info)
info.update({'city' : 'Delhi'})
print(info)

#clear() - used to remove all items from the dictionary.
info.clear()
print(info)

#pop() - used to remove the item with the specified key name.
info = {'name' : 'Ravi','age' : '21','eligible' : True}
print(info)
info.pop('age')
print(info)

#popitem() - used to remove the last inserted item (in versions before 3.7, it removes an arbitrary item).
info.popitem()
print(info)

#del() - used to remove the item with the specified key name.
info = {'name' : 'Ravi','age' : '21','eligible' : True}
print(info)
del info['age']
print(info)