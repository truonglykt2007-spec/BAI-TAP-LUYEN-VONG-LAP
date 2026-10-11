n = int(input())
temp = n
a = 0
while n > 0:
   a = a * 10 + (n % 10)
   n = n //10
if a == temp:
   print("Yes")
else:
   print("No")

