n = int(input())
for a in range(n , 0, -1):
    print(" " * (n - a) + "*" * ( 2 * a - 1))
for b in range(2, n + 1):
    print(" " * (n - b) + "*" * ( 2 * b -1))
