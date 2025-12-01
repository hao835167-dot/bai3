print("Tên: trần văn hào")
print("Msv:245752021610153")
print("#############################")
######################################
def benefit(t, n, k):
    """
    t: lãi suất theo % mỗi tháng (vd: 1.5 cho 1.5%)
    n: số vốn ban đầu
    k: số tháng gửi
    """
    # Chuyển lãi suất từ phần trăm sang số thập phân
    rate = t / 100

    # Tính số tiền sau k tháng theo công thức lãi kép
    final_amount = n * (1 + rate) ** k

    return final_amount

# Nhập dữ liệu từ bàn phím
try:
    t = float(input("Nhập lãi suất tiết kiệm (%/tháng): "))
    n = float(input("Nhập số vốn ban đầu: "))
    k = int(input("Nhập số tháng gửi: "))

    if t < 0 or n < 0 or k < 0:
        print("Các giá trị nhập phải không âm.")
    else:
        result = benefit(t, n, k)
        print(f"Số tiền nhận được sau {k} tháng là: {result:.2f}")
except ValueError:
    print("Vui lòng nhập đúng định dạng số.")

