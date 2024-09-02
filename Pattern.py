n1 = int(input("Enter number of rows: "))
for i in range(n1):
    for j in range(i + 1):
        print("*", end = " ")
    print()
n2 = int(input("Enter number of rows: "))
for i in range(1, n2 + 1):
    print(" " * (n2 - i) + "*" * (2 * i - 1))

n3 = int(input("Enter number of rows: "))
for i in range(1, n3 + 1):
    print(" " * (n3 - i) + "*" * (2 * i - 1))
for i in range(n3 - 1, 0, -1):
    print(" " * (n3 - i) + "*" * (2 * i - 1))