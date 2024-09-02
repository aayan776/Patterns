#Right_Angled_Triangle
n1 = int(input("Enter number of rows: "))
for i in range(n1):
    for j in range(i + 1):
        print("*", end = " ")
    print()
#Triangle
n2 = int(input("Enter number of rows: "))
for i in range(1, n2 + 1):
    print(" " * (n2 - i) + "*" * (2 * i - 1))
#Diamond
n3 = int(input("Enter number of rows: "))
for i in range(1, n3 + 1):
    print(" " * (n3 - i) + "*" * (2 * i - 1))
for i in range(n3 - 1, 0, -1):
    print(" " * (n3 - i) + "*" * (2 * i - 1))
#Floyd's_Triangle
number = 1
n4 = int(input("Enter number of rows: "))
for i in range(n4 + 1):
    for j in range(i + 1):
        print(number, end = " ")
        number += 1
    print()
#Reverse_Right_Angled_Triangle
n5 = int(input("Enter number of rows: "))
for i in range(n5, 0, -1):
    print("*" * i)
#Triangle_with_space
n6 = int(input("Enter number of rows: "))
for i in range(1, n6 + 1):
    if i == n6:
        print(" " * (n2 - i) + "*" * (2 * i - 1))
    else:
        print(" " * (n6 - i) + "*" + " " * (2 * i - 3) + "*")
#Floyd's Diamond
number2 = 1
n7 = int(input("Enter number of rows: "))
for i in range(1, n7 + 1):
    print(" " * (n7 - i) + str(number2) * (2 * i - 1))
    number2 += 1
for i in range(n3 - 1, 0, -1):
    print(" " * (n7 - i) + str(number2) * (2 * i - 1))
    number2 += 1
