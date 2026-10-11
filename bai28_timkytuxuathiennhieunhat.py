s = input()
dem = {}
for ky_tu in s:
    if ky_tu in dem:
        dem[ky_tu] += 1  
    else:
        dem[ky_tu] = 1  
so_lan_lon_nhat = 0
for ky_tu in dem:
    if dem[ky_tu] > so_lan_lon_nhat:
        so_lan_lon_nhat = dem[ky_tu]
ket_qua = []
for ky_tu in dem:
    if dem[ky_tu] == so_lan_lon_nhat:
        ket_qua.append(ky_tu)
print("Ký tự xuất hiện nhiều nhất là:", " ".join(ket_qua))