
num = int(input("Enter a number: "))
is_duck = False
while num > 0:
    if num % 10 == 0:
        is_duck = True
        break 
    num//=10
if is_duck:
    print("Duck Number")
else:
    print("Not a Duck Number")

"""
Enter a number: 011
Not a Duck Number

Enter a number: 101
Duck Number
"""