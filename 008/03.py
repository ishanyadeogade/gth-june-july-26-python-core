
i = 1
while i<=5:
    j=1
    flag=True
    while j<=9:
        if j>=6-i and j<=4+i and flag:
            print("*",end="")
            flag=False
        else :
            print(" ",end="")
            flag=True
        j+=1
    i+=1
    print()
    
"""
    *    
   * *   
  * * *  
 * * * * 
* * * * *  

""" 