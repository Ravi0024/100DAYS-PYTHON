""" 
    Finally keyword in python : the finally code block is also a part of exception handling.when we handle exception 
    using the try and except block.we can include a finally block at the end.The finall block is always executed,
    so it is a generally used for doing the concluding tasks like closing file resources or closig database connection or may be 
    ending the program execution with a delightful message.
#synatx:
try:
    #statements which could generate exception
except:
    #solution of generated exception
finally:
    #block of code which is going to execute in any situation

the finally block is exceuted irrespective of the outcome of try...except...else blocks
"""
def func1():
    try:
        l = [1,5,6,7]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("some error occured")
        return 0
    finally:
        print("I am always excueted")
    # print("I am always excueted")
x = func1()
print(x)






# One of the imp use cases of finally block is in a function which returns a value