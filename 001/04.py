
base = int(input("Enter a base : "))
index = int(input("Enter an index : "))
if index < 0 :
    print("Index should be a positive number")
elif index == 0 :
    print(1)
else :
    p = 1
    while index > 0:
        p = p * base;
        index-=1
    print(p)
"""
Enter a base : 3
Enter an index : 4
81
"""