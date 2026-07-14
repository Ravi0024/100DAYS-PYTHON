#while loops in python
'''while loops execute a block of code as long as a specified condition is true.As soon 
    as the condition becomes false, the loop terminates. The syntax for a while loop is:
while condition:
    # code block'''
# i=int(input("enter a number:"))
# while i<=5:
#     i=int(input("enter a number:"))
#     print(i)

count=5
while count>0:
    print(count)
    count-=1

#else with while loop: we can use an else statement with a while loop to specify a block of code 
# that will be executed when the loop condition becomes false.
x=12
while x>0:
    print(x)
    x-=3
else:
    print("loop has ended")

#do while loop: python does not have a built-in do-while loop like some other programming languages,
#  but we can achieve similar functionality using a while loop with a break statement.
"""do{
   # code block
}while condition"""