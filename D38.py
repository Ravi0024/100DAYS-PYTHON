"   Raising custom errors in python   : we can raise custom errors by using the raise keyword. "

salary = int(input("Enter salary amount:"))
if not 2000 < salary < 5000:
    raise ValueError("Not a valid salary")

"""
    Defining Custom Exceptions : we can define custom exceptions by creating a 
                                new class that is deirved from the built-in eception class
syntax:
class CustomError(Exception):
    #code...
    pass
try:
    #code...
except CustomError:
    #code...

This is useful because sometimes we might want to do something when a particular exception is raised.
For example,sending an error report to the admin,calling an api,etc"""