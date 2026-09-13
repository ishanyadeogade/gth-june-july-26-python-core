
i=1 
while i<=9:
    j=1
    while j<=5:
        if j<=i and (i+j)<=10:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j+=1
    i+=1
    print()

"""

*         
* *       
* * *     
* * * *   
* * * * * 
* * * *   
* * *     
* *       
*   

"""