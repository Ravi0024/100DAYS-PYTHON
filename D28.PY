" String formatting in python - can be done using format method "
#txt = "for only {price : .2f} dollars!"
#print(txt.formatn {price = 49})

letter = "hey my name is {} and i am from {}"
name = "Raviteja"
country = "india"
print(letter.format(name, country))

' f-strings in python'
""" it is a new string formatting mechanism introduced by the PEP 498.
    the primary focus of  this mechanism is to make the interpolation easier.
    when we prefix the string with the letter "f",the string becomes the f-string itself.
     it can be formatted same as the str.format() method. """
#example : 

print(f"hey my name is {name} and i am from {country}")

' if we use double curly brackets '
print('we use f-strings like this 'f"hey my name is {{name}} and i am from {{country}}")

price = 12.121212
txt = f"for only {price : .2f} dollars!"
print(txt)

' we can also use single statement '
print(f"{2*3}")
print(type(f"{2*3}"))