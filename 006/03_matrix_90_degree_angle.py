
i = 1
while i <= 5:
    j = 1
    while j <= 5:
        if j==1:
            print("*",end=" ")
        elif i==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j += 1
    print()
    i += 1

"""
*         
*         
*         
*         
* * * * * 


i = 1
while i <= 5:
    j = 1
    while j == 1 or ( i==5 and j <= 5 ):
        print("*", end=" ")
        j += 1
    print()
    i += 1
   
"""   