#functions in python
"""A Function is a block of code that performs a specific task whenever it was called.
1.built-in functions
2.user defined functions"""

'built-in functions are pre coded in python'
'ex: min(),max(),len(),sum(),type(),range(),dict(),list(),tuple(),set(),print(),etc,.. '

a=2
b=3

"user-defined functions are the functions that we are created to perform the tasks as per our needs"
#syntax:  
# def function_name(parameters):          
#   pass
#code and statements
'create a function using the def keyword,followed by a function name,followed by a paranthesis() and a colon(:)'
'any parameters and arguments should be placed within the paranthesis'
'rules to naming the function should be same as the variables'
'any statements and other codes within the function should be indented '
def calculateGmean(a ,b):
    mean=(a*b)/(a+b)
    print(mean)