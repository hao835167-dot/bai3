print("Tên: trần văn hào")
print("Msv:245752021610153")
print("#############################")
######################################
import math

def Tinh(R):
    #Kiểm tra bán kính hợp lệ
    if R <= 0:
        return "Bán kính phải là số dương!"


    chu_vi = 2 * math.pi * R
    dien_tich = math.pi * R ** 2


    return f"chu vi = {chu_vi:.2f}, Diện tích = {dien_tich:.2f}"


#---chương trình chính---
try:
    R = float(input("Nhập bán kính hình tròn R = "))
    print(Tinh(R)
except valueError:
    print("Vui lòng nhập một số hợp lệ!")
    

