#if else conditional statements in python-'sometimes the programmer needs to execute a block of code only if a certain condition is true.
#  In such cases, we can use the if statement. The syntax of the if statement is as follows:
# if condition:
#     # block of code to be executed if the condition is true
# The condition is an expression that evaluates to either true or false. If the condition is true, the block of code inside the if statement will be executed. If the condition is false, the block of code will be skipped and the program will continue with the next statement after the if block.

a=int(input("enter your age: "))
print("your age is:",a)
if a>=18:
    print("you can drive")
else:
    print("you cannot drive")

#conditional operators are >,<,>=,<=,==,!=
# print(a>18) 
# print(a<18)
# print(a>=18)
# print(a<=18)
# print(a==18)
# print(a!=18)

"if"
"if else"
"if elif else"
"nested if else"

num=int(input("enter a number: "))
if num>0:
    print("the number is positive")
elif num<0:
    print("the number is negative")
else:
    print("the number is zero")


#if elif elif else
marks=int(input("enter your marks:"))
if marks>=90:
    print("grade A")
elif marks>=80:
    print("grade B")
elif marks>=70:
    print("grade C")
else:
    print("grade D")

#nested if else
num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
if num1>num2:
    print("num1 is greater than num2")
else:
    if num1<num2:
        print("num2 is greater than num1")
    else:
        print("num1 and num2 are equal")