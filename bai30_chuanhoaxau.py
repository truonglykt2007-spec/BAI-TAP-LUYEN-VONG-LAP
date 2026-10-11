s = input()
danh_sach_tu = s.split()
danh_sach_chuan_hoa = []
for tu in danh_sach_tu:
    tu_moi = tu.capitalize() 
    danh_sach_chuan_hoa.append(tu_moi)
ket_qua = " ".join(danh_sach_chuan_hoa)
print(ket_qua)

