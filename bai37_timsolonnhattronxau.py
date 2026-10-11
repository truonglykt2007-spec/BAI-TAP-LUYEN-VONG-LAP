s = input().strip('"')
a = s.replace('a', ' ').split()
so = ""
ds = []
for i in s:
    if i.isdigit():
        so = so + i
    else:
        if so != "":
            ds.append(int(so))
            so = ""
if so != "":
    ds.append(int(so))
print(max(ds))