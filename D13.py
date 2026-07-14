#STRINGS METHODS IN PYTHON
'Python provides a set of built-in methods that we can use to alter and modify the strings'
#upper()-this method converts the string into uppercase characters
str1="ravi teja"
print(str1.upper())

#lower()-this method converts the string into lowercase characters
str2="rAvITeja"
print(str2.lower())

#strip()-this method removes the white spaces before and after the string
str3=" RAVIteja "
print(str3.strip())

#rstrip()-it removes the trailing characters in the string
str4="rAvi!!!!"
print(str4.rstrip('!'))

#replace()-it replaces all the occurances of a string with another string 
str5="chiipuru"
print(str5.replace('i','e'))

#split()-it splits the given string at the specified instance and return the separated string as list items
str6="ravi teja"
print(str6.split(' '))

#captalize()-it turns only the first character of sring to upper case and the rest chars of the string are turned to lowercase. The string has no effect if the first letter is in uppercase
str7="ravi teja"
capstr7=str7.capitalize()
print(capstr7)

str8="ravi"
capstr8=str8.capitalize()
print(capstr8)

str9="Ravi"
capstr9=str9.capitalize()
print(capstr9)

#center()-it aligns the string to the center as per the parameters given by the user
str10="ravi teja"
centerstr10=str10.center(20,' ')
print(centerstr10)

centerstr10=str10.center(20,'*') # it will align the string to the center and fill the remaining space with *
print(centerstr10)

#count()-it counts the number of occurances of a substring in the given string
str11="ravi teja"
print(str11.count('a')) # it will count the number of times 'a' occurs in the string
 
#endswith()-it checks if the string ends with the specified suffix and returns true or false
str12="ravi teja"
print(str12.endswith('a')) # it will return true because the string ends with 'a

'we can also check for a value in between the string ends with the given value'
print(str12.endswith('teja',4,10)) # it will return true because the string ends with 'teja' between index 5 and 10

#find()-it finds the first occurrence of the specified value and returns the index number of the first character of the first occurrence. If the value is not found, it returns -1
str13="ravi teja"
print(str13.find('teja')) # it will return 5 because 'teja' starts at index 5

#isalnum()-it checks if all the characters in the string are alphanumeric and returns true or false
str14="ravi123"
print(str14.isalnum()) # it will return true because all the characters in the string are alphanumeric
str15="ravi teja"
print(str15.isalnum()) # it will return false because there is a space in the

#isalpha()-it checks if all the characters in the string are alphabetic and returns true or false
str16="ravi"    
print(str16.isalpha()) # it will return true because all the characters in the string are alphabetic
str17="ravi123"
print(str17.isalpha()) # it will return false because there are numbers in the string

#islower()-it checks if all the characters in the string are lowercase and returns true or false
str18="ravi"    
print(str18.islower()) # it will return true because all the characters in the string are lowercase

#isprintable()-it checks if all the characters in the string are printable and returns true or false
str19="ravi teja"
print(str19.isprintable()) # it will return true because all the characters in the string are printable
str20="ravi teja\n"
print(str20.isprintable()) # it will return false because there is a newline character in the string    

#isspace()-it checks if all the characters in the string are whitespace and returns true or false
str21="   "
print(str21.isspace()) # it will return true because all the characters in the string are whitespace

#istitle()-it checks if the string follows the title case and returns true or false. A string is in title case if all the words in the string start with a capital letter and the rest of the characters are in lowercase
str22="Ravi Teja"
print(str22.istitle()) # it will return true because the string follows the title case
str23="Ravi teja"
print(str23.istitle()) # it will return false because the second word in the string does not start with a capital letter
 
#isupper()-it checks if all the characters in the string are uppercase and returns true or false

#islower()-it checks if all the characters in the string are lowercase and returns true or false

#startwith()-it checks if the string starts with the specified prefix and returns true or false
str24="ravi teja"
print(str24.startswith('ravi')) # it will return true because the string starts with 'ravi'
print(str24.startswith('teja')) # it will return false because the string does not start with 'teja'

#swapcase()-it converts all the uppercase characters in the string to lowercase and all the lowercase characters to uppercase
str25="Ravi Teja"
print(str25.swapcase()) # it will convert all the uppercase characters to lowercase and all the lowercase characters to uppercase

#title()-it converts the first character of each word in the string to uppercase and the rest of the characters to lowercase
str26="ravi teja"
print(str26.title()) # it will convert the first character of each word to uppercase and the rest to lowercase