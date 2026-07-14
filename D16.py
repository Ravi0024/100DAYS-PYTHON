#Match case statement in Python
'''To match a value against multiple cases, you can use the match statement in Python. 
The match statement is a powerful control flow structure that allows you to compare a value against
 multiple patterns and execute code based on the first matching pattern. 
  
the match case consist of 3 main entities:
1. The match keyword: This is used to start the match statement and indicates that you want to compare a value against multiple cases.
2. one or more case blocks: Each case block starts with the case keyword followed by a pattern to match against the value.
                             The code inside the case block will be executed if the pattern matches.
3. Expression for each case: This is the code that will be executed if the pattern in the case block matches the value being compared. 
                             You can have multiple lines of code in each case block, and you can also use the break statement to exit the match statement after a case has been executed.
'''
'''syntax:
match variable_name:
    case pattern1:
        # code to execute if pattern1 matches
    case pattern2:
        # code to execute if pattern2 matches
    case _:
        # code to execute if no patterns match (optional)'''

#Example of match case statement in Python
def get_day_name(day_number):
    day_number = int(input("Enter a day number (1-7): "))
    match day_number:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid day number"