" Recursion in python - is the process of defining something in terms of itsef "
''' A physical world example would be to place 2 parallel mirrors facing each other.
    Any object in between them would be reflected recursively.'''
#python recursivemfunction
"""in python ,we know that a function can call other functions. it is possible for the function to 
    to call itself.These types of construct are termed as recursive functions."""
#example:
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
# print(factorial(12))
# print(factorial(0))
num = int(input("ENTER A NUMBER : "))
print("Factorial : ",factorial(num))

" write a program to print Fibonacci sequence using recursion"
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
num = int(input("Enter a number for fibonacci sequence : "))
for i in range(num):
    print(fib(i),end=" ")