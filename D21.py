#function arguments and return statement in python
"""4 types are:
                1.Default arguments: in this type we provide deafult value while creating a function.
                                    This way the function  assumes a default value even if a value is not 
                                    provided in the function call for that argument"""
#ex:
def average(a=2,b=4):
    print ("the avarage is ",(a+b)/2)
average(a=10)


"""
                2.keyword arguments: we can provide arguments with key= value ,this way the the interpreter 
                                    recognizes the arguments by the parameter name.Hence, the order in which 
                                    the arguments are passed does not matter"""
#ex
def name(fname  ,mname = "Teja" ,lname = "C Rt"):
   print("Hello, " , fname , mname ,lname)
name("Ravi")


"""             
        3.Required arguments: in case we dont pass the arguments with a key-value syntax then it is necessary to pass the arguments in the correct positional order
                            and the no of arguments passed should match with actual function defnition.

                            ex:when no of arguments passed does not match the actual function defnition """
def name(fname, mname, lname):
    print("hello ,", fname ,mname ,lname)
name("ravi" ,"teja" ,"crt")



""" 
     4.variable-length arguments : Sometimes we may need to pass more arguments than those defined in the actual function.This can be done using variable-length arguments
                                    their are 2 ways to achieve this:

                            1. Arbitrary arguments: while creating a function, pass  a* before parameter name while defining the function.
                                                    the fun access the argus by processing them in the form of tuples"""
                        #ex:
                        def name(*name):
                            print("hello ,",name[1] ,name[2] ,name[3])
                        name('Rav' , 'Tej' ,'CRT')

                          """  2.Keyword arbitrary arguments:while creating a func , pass a* before the parameter name while defining the func.
                          the func accesses the arguments by processing them in the form of dictionary
ex:"""
def name(**name):
    print{"hello,", name["fname"], name["mname"] ,name["lname"]}
name{mname = "buci" , lname = "boka" , fname = "jak"}



#return statement in python- is used to return the value of the expression back to the calling func
#ex:
def name(fname, mname ,lname):
      return "hello ," * + fname + * * + mname + * * + lname 
print(name("roug" ,"rascal" ,"rowdy"))
