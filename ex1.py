# a
print("*"*20)

# b
n = int(input("Enter the number of star(s) "))
print("*"*n)

# c
for i in range(9):
    if i %2 == 0:
        print("x", end="")
    else:
        print("*", end = "")
print()

# d
numbers = int(input("Enter the number of star(s) "))
for i in range(numbers):
    if i %2 == 0:
        print("x", end="")
    else:
        print("*", end = "")
print()

# f
for i in range(3):
    print("*"*7)

# g
new_n = int(input("Enter the columns "))
new_m = int(input("Enter the rows "))
for i in range(new_m):
    print("*"*new_n)

# h
for i in range(5):
    if i != 3:
        print("-"*6)
    if i == 3:
        for j in range(6):
            if j == 1:
                print("x", end = "")
            else:
                print("-", end = "")
        print()

# i
w = int(input("enter the width "))
h = int(input("enter the height "))
x = int(input("enter the position x "))
y = int(input("enter the position y "))
for a in range(h):
    if a != y:
        print("-"*w)
    if a == y:
        for b in range(w):
            if b == x:
                print("x", end = "")
            else:
                print("-", end = "")
        print()