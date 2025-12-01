import math

def Tinh(R):
    # Kiểm tra giá trị bán kính đầu vào
    if R <= 0:
        print("Bán kính phải là một số dương.")
        return

    # Tính chu vi và diện tích
    chu_vi = 2 * math.pi * R
    dien_tich = math.pi * R ** 2

    # In kết quả
    print(f"Chu vi hình tròn: {chu_vi:.2f}")
    print(f"Diện tích hình tròn: {dien_tich:.2f}")

# Nhập bán kính từ bàn phím và gọi hàm
try:
    R = float(input("Nhập bán kính hình tròn: "))
    Tinh(R)
except ValueError:
    print("Vui lòng nhập một số hợp lệ.")
