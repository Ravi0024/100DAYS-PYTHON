"   short hand if-else statements    "
"""
If...Else in One Line
there is also a shorthand syntax for the if-else statement that can be
used when the condition being tested is simple and the code blocks
to be executed are short 
example:"""
a=21
b=2
print("A") if a > b else print("B")

#you can also have multiple else statements on the same line:
#one line if else statements on the same line:
a=330
b=333  
print("A") if a > b else print("=") if a==b else print("B")

#another example
result = value_if_true if condition else value_if_false

"this syntax is equivalent to the following if-else statement : "
# if condition:
#     result = value_if_true
# else:
#     result = value_if_false

"""
CONCLUSION:
THE SHORTHAND IF-ELSE STATEMENT IS A CONVENIENT WAY TO WRITE SIMPLE-IF-ELSE STATEMENTS,
ESPECIALLY WHEN YOU WANT TO ASSIGN A VALUE TO A VARIABLE BASED ON A CONDITION.
however, it's not suitable for more complex situations where you need to execute
multiple statements or perform more complex logic.in those cases,it's best to use
the full if-else syntax
 
"""