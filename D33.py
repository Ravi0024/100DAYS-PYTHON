"   DICTIONARIES IN PYTHON   - are ordered collection of items .they store multipe items in a single variable."
"key:valiue pirs that are separeted by commas and enclosed within curly brackets{} "
info = {'name' : 'Ravi','age' : '21','eligible' : True}
print(info)
print(info['name'])

# 1. Accessing single items - we can access single items by referring to its key name, inside square brackets. or by using the get() method.
data = {111: 'Ravi', 222: 'Ramesh', 333: 'Suresh'}
print(data[222])
print(info.get('data'))

# 2. Accesing multiple items - we can access multiple items by using a values() method. it returns a list of all the values in the dictionary.
print(info.values())
print(data.values())
for i in info.values():
    print(i)

# 3. Accessing keys - we can access keys by using the keys() method. it returns a list of all the keys in the dictionary.
print(info.keys())

# 4.Accssing key-value pairs - we can access key-value pairs by using the items() method. it returns a list of tuples, each tuple contains a key-value pair.
print(info.items())