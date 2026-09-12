
num = int(input("Enter a number: "))
i = 1
sum = 0
while i <= num/2:
    if num % i == 0:
        sum+=i
    i+=1

if sum == num:
    print("Perfect Number")
else:
    print("Not a Perfect Number")

"""
Enter a number: 6
Perfect Number

Enter a number: 3
Not a Perfect Number

Enter a number: 28
Perfect Number
"""

