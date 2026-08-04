"""   Exception handling in python    
    It is the process of responding to unwanted or unexpected events when a computer program runs.
   Exception handling deals with these events to avoid the program or system crashing,and without this process
   exceptionswould disrupt the normal operation of a program.  
"""
#Exceptions in python
''' Python has many built-in exceptions that are raised when your program
    encounters an error (something in the program goes wrong)
    
    when these exceptions occur,the python interpreter stops the current process
    and passes it to the calling process until it is handled.If not handled,the program will crash.
'''

#Python try...except
''' try...except blocks are used in python to handle errors and exceptions.The code
    in try block runs when there is no error.If the try block catches the error,then the excet block is executed.
'''
#Syntax:
"""
try:
    #statements which could generate
    #exception
except:
"""
#example:
try:
  num=int(input("enter an integer:"))
  a=[6,3]
  print(a[num])
except ValueError:
  print("number entered is not an integer.")
except IndexError:
  print("number enterd is not an integer ")

a = input("Enter the number:")
print(f"Multiplication table of {a} is:")
try:
 for i in range(1,11):
    print(f"{int(a)}x{i}={int(a)*i}")
except Exception as e:
  print("Invalid input!")
print("End of program")


