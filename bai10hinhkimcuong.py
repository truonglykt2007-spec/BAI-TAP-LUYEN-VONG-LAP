n = int(input())
for a in range(1, n + 1):
    print(" " * (n - a), end= "")
    for b in range(1, 2 * a):
        if b == 1 or b == 2 * a -1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
for a in range(n - 1, 0, -1):
    print(" " * (n - a), end= "")
    for b in range(1, 2 * a):
        if b == 1 or b == 2 * a - 1:
            print("*", end= "")
        else:
            print(" ", end= "")
    print()

    
        