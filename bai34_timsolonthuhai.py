chuoi_nhap = input("Hãy nhập các số, cách nhau bằng dấu cách: ")

numbers = [int(x) for x in chuoi_nhap.split()]

unique_numbers = list(set(numbers))
if len(unique_numbers) < 2:
    print("Dãy số phải có ít nhất 2 số khác nhau!")
else:
    danh_sach_sap_xep = sorted(unique_numbers)
    so_lon_nhi = danh_sach_sap_xep[-2]
    
    print("Dãy số bạn đã nhập:", numbers)
    print("Số lớn thứ hai là:", so_lon_nhi)
