

i = 1
while i<=5:
    j=1
    while j<=9:
        if j<=(6-i) or j>=(4+i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j+=1
    i+=1
    print()
    

"""

* * * * * * * * * 
* * * *   * * * * 
* * *       * * * 
* *           * * 
*               * 


5  5
4  6 
3  7
2  8
1  9

"""