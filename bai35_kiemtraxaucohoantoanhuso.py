s = input()
s = s.strip('"')
dem = 0
for i in s:
    if i >= '0' and i <= '9':
        dem += 1
if dem == len(s):
    print("YES")
else:
    print("NO")