
num = int(input("Enter a number: "))
digit = int(input("Enter a digit to search: "))
found = False 

while num > 0:
    if num % 10 == digit:
        found = True 
        break 
    num//=10
if found:
    print("Digit Found")
else :
    print("Digit Not Found")

"""
Enter a number: 345
Enter a digit to search: 4
Digit Found

Enter a number: 0567
Enter a digit to search: 0
Digit Not Found
"""