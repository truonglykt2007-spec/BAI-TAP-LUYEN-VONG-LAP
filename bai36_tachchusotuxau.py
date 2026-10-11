s = input().strip('"')
so = ""
for i in s:
    if i.isdigit():
        so = so + i
    else:
        if so != "":
            print(so, end=" ")
            so = ""
if so != "":
    print(so)