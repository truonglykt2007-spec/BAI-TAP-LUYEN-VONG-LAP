n = int(input())
so = n
dem = 0
if n == 0:
    dem = 1
else:
    while so > 0:
        so //= 10  
        dem += 1     
print(f"Số lượng chữ số của {n} là: {dem}")
