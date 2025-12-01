print("Tên: trần văn hào")
print("Msv:245752021610153")
print("#############################")
######################################
import math

def Tinh(R):
    # Kiểm tra bán kính hợp lệ
    if R <= 0:
        print("Bán kính không hợp lệ! Bán kính phải lớn hơn 0.")
        return None, None
    
    # Tính chu vi và diện tích
    chu_vi = 2 * math.pi * R
    dien_tich = math.pi * R * R
    
    return chu_vi, dien_tich

# Chương trình chính
try:
    R = float(input("Nhập bán kính hình tròn R: "))
    
    cv, dt = Tinh(R)
    
    if cv is not None and dt is not None:
        print(f"Chu vi hình tròn với bán kính {R} là: {cv:.2f}")
        print(f"Diện tích hình tròn với bán kính {R} là: {dt:.2f}")
        
except ValueError:
    print("Lỗi: Vui lòng nhập số hợp lệ!")
