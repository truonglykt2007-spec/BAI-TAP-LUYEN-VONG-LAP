n = int(input())
for a in range(1, n + 1):
    for b in range(1, 2 *n):
        if a == n  or a + b == n + 1 or b - a == n - 1 :
            print("*", end= "")
        else:
            print(" ", end= "")
    print()    