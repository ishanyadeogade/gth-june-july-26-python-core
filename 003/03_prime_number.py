
num = int(input("Enter a number: "))
is_prime = True
i = 2
while i <= num/2:
    if num % i == 0:
        is_prime = False
        break
    i+=1
if is_prime:
    print("Prime Number")
else:
    print("Not a Prime Number")

"""

Enter a number: 6
Not a Prime Number

Enter a number: 7
Prime Number

Enter a number: 11
Prime Number

"""

