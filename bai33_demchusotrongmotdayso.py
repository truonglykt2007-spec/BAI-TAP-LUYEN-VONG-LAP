n = int(input())
a = input().split()
dem = 0
for i in range(n):
    dem += len(a[i])
print(dem)