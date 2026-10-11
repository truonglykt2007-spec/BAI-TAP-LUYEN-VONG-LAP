import sys

def tinh_tong_chu_so(num):
    # Chuyển số thành chuỗi để duyệt qua từng ký tự chữ số
    return sum(int(digit) for digit in str(abs(num)))

def main():
    # Đọc toàn bộ dữ liệu đầu vào từ bàn phím (bất kể xuống dòng hay cách nhau khoảng trắng)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    # Xử lý trường hợp chuỗi nhập vào có dạng "n=5" hoặc chỉ là số "5"
    first_item = input_data[0]
    if "=" in first_item:
        n = int(first_item.split("=")[1])
        numbers = [int(x) for x in input_data[1:n+1]]
    else:
        n = int(first_item)
        numbers = [int(x) for x in input_data[1:n+1]]
    
    if not numbers:
        return

    max_sum = -1
    result = None

    for num in numbers:
        current_sum = tinh_tong_chu_so(num)
        
        # Nếu tìm thấy tổng lớn hơn, cập nhật kết quả
        if current_sum > max_sum:
            max_sum = current_sum
            result = num

    print(result)

if __name__ == "__main__":
    main()