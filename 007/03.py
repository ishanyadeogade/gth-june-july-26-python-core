
i=1 
while i<=5:
    j=1
    while j<=9:
        if (i+j)>=6 and (j-i)<=4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j+=1
    i+=1
    print()

"""

        *         
      * * *       
    * * * * *     
  * * * * * * *   
* * * * * * * * * 

"""