
num = int(input("Enter a number: "))
digit_count = 0 
temp = num 

while num > 0 :
    digit_count += 1
    num //= 10 

digit_count -= 1
num = temp 

first_digit = num // 10**digit_count
last_digit = num % 10 

# removing the first digit
num = num % 10**digit_count

# removing the last digit
num = num // 10;

result = last_digit*(10**digit_count) + num*10 + first_digit

print(result)

"""
Enter a number: 1234
4231

Enter a number: 0456
654

Enter a number: 012340
2341
"""





