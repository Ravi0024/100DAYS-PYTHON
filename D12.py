# STRING SLICING AND OPERATIONS ON STRING
'''we can find the length of the string using len() function'''

name="Ravi teja"
print(len(name)) # it will print the length of the string

#string as a array
"we can access the characters of the string using index number and we can also slice the string using index number"
print(name[2]) # it will print the third character of the string
print(name[0:4]) # it will print the characters from index 0 to 3
print(name[5:]) # it will print the characters from index 5 to the end of the string
print(name[:5]) # it will print the characters from the beginning of the string to index 4
print(name[-1]) # it will print the last character of the string

#looping through the string
for i in name:
    print(i) # it will print each character of the string in a new line