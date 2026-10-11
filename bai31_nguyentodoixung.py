def la_so_doi_xuong(n):
    chuoi = str(n)
    return chuoi == chuoi[::-1]
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:  
            return False
    return True
n = int(input())
print(f"Các số nguyên tố đối xứng từ 1 đến {n} là:")
for i in range(1, n + 1):
    if la_so_doi_xuong(i) and la_so_nguyen_to(i):
        print(i, end=" ")
