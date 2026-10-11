n = int(input())
for m in range(1, n + 1):
    print("  " * (n - m) + "*" * (2 * m - 1))