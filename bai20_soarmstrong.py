def is_armstrong(n):
  str_n = str(n)
  k = len(str_n)
  total = sum(int(digit) ** k for digit in str_n)
  return total == n
num = int(input())
if is_armstrong(num):
  print("YES")
else:
  print("NO")

