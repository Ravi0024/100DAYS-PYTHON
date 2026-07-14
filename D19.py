#break and continue statements in python
"BREAK statement enables a program to skip over a part of the code."
"A break statement is used to terminates the every loop it lies within"
# for i in range(1,101,1):
#     print(i , end=" ")
#     if(i==50):
#         break
#     else :
#         print("RAVITEJJA")
#     print("thank you")

#continue statement skips the resst of the loop STATEMENTS and causes the next iteratiojn over
for i in [2,3,4,6,8,0]:
    if (i%2!=0):
        continue
    print(i)


    """do while loop in which a set of instructions will exexcute at once (irrespective of condition) and then the
    repetation of the loop depends on the condition passed at the end of while loop .It also known as exit-controlled loop"""