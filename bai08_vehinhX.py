n = int(input())
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b or a == (n - b + 1):
            print("*", end= " ")
        else:
            print(" ", end=" ")
    print()