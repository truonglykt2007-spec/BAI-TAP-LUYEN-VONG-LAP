s = input()
nguyen_am_list = "aeiouAEIOU"
so_nguyen_am = 0
so_phu_am = 0
for ky_tu in s:
    if ky_tu.isalpha():
        if ky_tu in nguyen_am_list:
            so_nguyen_am += 1  
        else:
            so_phu_am += 1     
print("Số nguyên âm là:", so_nguyen_am)
print("Số phụ âm là:", so_phu_am)