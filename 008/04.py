
i=1
while i<=9:
    j=1
    while j<=9:
        if i<=5 and j>=6-i and j<=4+i:
            print("*",end="")
        elif i>5 and j>=i-4 and j<=14-i:
            print("*",end="")  
        else:
            print(" ",end="")
        j+=1
    i+=1
    print()

    """
    
    *    
   ***   
  *****  
 ******* 
*********
 ******* 
  *****  
   ***   
    *    

    """
