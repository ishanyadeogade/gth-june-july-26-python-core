
num = int(input("Enter a number: "))
digit_count = 0
temp = num 
while num > 0 :
    digit_count += 1
    num //= 10 

num = temp 
sum = 0
while num > 0 :
    rem = num % 10
    sum = sum + rem**digit_count 
    num //= 10 

if sum == temp :
    print("Armstrong Number")
else :
    print("Not an Armstrong Number")

"""
Enter a number: 11
Not an Armstrong Number

Enter a number: 153
Armstrong Number

Enter a number: 9
Armstrong Number

"""



    

    


