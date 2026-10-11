n = int(input())
for a in range(2, n + 1):
    is_prime = True
    for b in range(2, int(a ** 0.5) + 1):
        if a % b == 0:
           is_prime = False
           break
    if is_prime:
        print(a, end=' ')