n = int(input())
dao_nguoc = 0
while n > 0:
    phan_du = n % 10
    dao_nguoc = (dao_nguoc * 10) + phan_du
    n = n // 10
print("Dao nguoc:", dao_nguoc)