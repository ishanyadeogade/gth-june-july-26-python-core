
base = int(input("Enter a base : "))
index = int(input("Enter an index : "))
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