
"""

Q3. Write a java program to print this pattern.

	*	#	*	#	*
	*	#	*	#	*
	*	#	*	#	*
	*	#	*	#	*
	*	#	*	#	*

"""

i = 1
while i <= 5 :
    j = 1 
    while j <= 5 : 
        if j%2 == 0 :
            print("#", end="   ")
        else :
            print("*", end="   ")
        
        j += 1
    print()
    i += 1

"""
*   #   *   #   *   
*   #   *   #   *   
*   #   *   #   *   
*   #   *   #   *   
*   #   *   #   *  
"""
