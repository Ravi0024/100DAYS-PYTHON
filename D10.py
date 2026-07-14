#Taking user input in python
'''In python ,we can take user input using the input() function.this input() function 
    reads a line from the input and returns it as a string.
    so we pass it to the variable name to store the user input.'''
name = input("Enter your name: ")
print("Hello, " + name + "! Welcome to Python programming.")

"Always the input function returns a string, so if you want to take a different data type as input,"
" you need to convert it using type casting."

age = int(input("Enter your age: "))
print("You are " + str(age) + " years old.")

height = float(input("Enter your height in meters: "))
print("Your height is " + str(height) + " meters.") 

'''You can also take multiple inputs from the user in a single line using the split() method.
The split() method splits the input string into a list of substrings based on a specified delimiter (default is space).'''
#Example:
input_data = input("Enter your name, age, and height (separated by space): ")
name, age, height = input_data.split()  # splitting the input into three parts  
age = int(age)  # converting age to integer
height = float(height)  # converting height to float

print("Name: " + name)
print("Age: " + str(age))
print("Height: " + str(height) + " meters")
'''In the above example, we take multiple inputs from the user in a single line, split them into separate variables,
     and then convert the age and height to the appropriate data types.'''
