
"""
Q5. Write a java program to print this pattern.

*****
****
***
**
*


"""

i=1 
while i<=5:
    j=5
    while j>=1:
        if(j >= i):
            print("*",end="")
        else:
            print(" ",end="")
        j-=1
    i+=1
    print()
    
"""

*****
**** 
***  
**   
* 
 
"""