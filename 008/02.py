
i = 1
while i<=10:
    j=1 
    while j<=10:
        
        if ( i<=5 and ( j<=i or j>(10-i) ) ) or ( i>5 and ( j<=10-i or j>i ) ):
            print("*",end=" ")
        else :
            print(" ",end=" ")
            
        j+=1 
    i+=1
    print()

"""

*                 * 
* *             * * 
* * *         * * * 
* * * *     * * * * 
* * * * * * * * * * 
* * * *     * * * * 
* * *         * * * 
* *             * * 
*                 * 

"""   
