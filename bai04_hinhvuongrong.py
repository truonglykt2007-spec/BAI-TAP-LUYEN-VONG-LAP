n = int(input())
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == 1 or a == n or b == 1 or b == n:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()