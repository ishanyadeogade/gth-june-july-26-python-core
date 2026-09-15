
# skin a digit in a number which is multiple of 3 

num = int(input("Enter a number : "))

temp = num 
digit_count = 0

while num>0:
    digit_count+=1
    num//=10

digit_count-=1
num = temp 
new_num = 0

while num>0:
    quotient = num//(10**digit_count)
    num = num%(10**digit_count)
    if quotient%3==0:
        new_num = new_num*10+quotient;
        
    digit_count-=1
    
print(new_num)

"""

Enter a number : 123456
36

Enter a number : 987654
96

Enter a number : 1001344783
33

"""

