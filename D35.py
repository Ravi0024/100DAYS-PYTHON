" for loop with else in python "
""" python allows the else keyword to be used with the for and while loops too. The else block appears after the 
    body of the loop.the stateents in the else block will be executed after all iterations are completed.
    The program exists the loop only after the else block is executed."""
"syntax"
#for counter in sequence:
    #statements inside the loop block"
# else:
    ##statements inside else block


for i in range(5):
    print("iteration no {} in for loop".format(i+1))
else:
        print("sorry i isn't found")
print("out of loop")