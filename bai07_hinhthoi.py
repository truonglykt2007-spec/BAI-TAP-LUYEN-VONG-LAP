n = int(input())
for m in range(1, n + 1):
    print(" " * (n - m) + "*" * (2 * m - 1))
for a in range(n -1, 0, -1):
    print(" " * (n - a) + "*" * (2 * a - 1))