#Docstrings in python - are the string literals that appear right after the definition of a function ,method, class or module.
#ex:
def square(n):
    '''takes a number n and returns the square of n'''
    print(n**2)
square(5)

#here the text in the ''' ''' quotes is a docstring which are not appear in python

"to print doc string"
print(square.__doc__)
'We can change comments so the program wouldnt change but if we change doc string the program will change '

#python comments - comments are the descriptions that help programmers better understand the intent and functionality of the program .they are completly ignored by the interpretor
# doc-strings - this are strings after the definition of a function method,class,or module they are used to document our code.we can access these docstrings using the doc attribute.
#pyhton doc attribute - whenever string laterals are present just after the definition of a function ,module,class  or method,they are associated with the object as their doc attribute.we can later use this attribute to retrive the docstring.

""" PEP 8 (python enhancement proosal) is a document that provides guidelines and best practices on how to write python code.
    the primary focus of pep 8 is to improve the readability and consistency of the python code """

#the zen of python
import this#execute it and see