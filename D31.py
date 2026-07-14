"   SETS IN PYTHON    "
""" SETS ARE UNORDERED COLLECTIONS OF UNIQUE ELEMENTS. THEY ARE MUTABLE, MEANING YOU CAN ADD OR REMOVE 
    ELEMENTS AFTER THE SET HAS BEEN CREATED. SETS ARE USEFUL FOR MEMBERSHIP TESTING, ELIMINATING DUPLICATES FROM A SEQUENCE,
      AND PERFORMING MATHEMATICAL OPERATIONS LIKE UNION, INTERSECTION, DIFFERENCE, AND SYMMETRIC DIFFERENCE.
   SETS ARE DEFINED USING CURLY BRACES {} OR THE set() FUNCTION. 
   sets doesnot contain duplicate elements. if we try to add duplicate elements to a set, it will be ignored."""
s={1,1,2,3,4}
print(s)

info = {"ravi",21, True,5.8,21}
print(info)

#accessing elements in a set
for value in info:
    print(value)

ravi=set()
print(type(ravi))