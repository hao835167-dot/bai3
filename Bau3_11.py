def benefit(t, n, k):
    """
    Tính số tiền nhận được sau k tháng gửi tiết kiệm
    t: lãi suất %/tháng
    n: số vốn ban đầu
    k: số tháng gửi
    """
    # Chuyển lãi suất từ % sang số thập phân
    lai_suat = t / 100
    
    # Tính số tiền nhận được theo công thức lãi kép
    so_tien_nhan_duoc = n * (1 + lai_suat) ** k
    
    return so_tien_nhan_duoc

# Chương trình chính
try:
    # Nhập dữ liệu từ bàn phím
    t = float(input("Nhập lãi suất tiết kiệm (%/tháng): "))
    n = float(input("Nhập số vốn ban đầu: "))
    k = int(input("Nhập số tháng gửi: "))
    
    # Kiểm tra điều kiện đầu vào
    if t < 0 or n <= 0 or k <= 0:
        print("Lỗi: Lãi suất không được âm, vốn và số tháng phải lớn hơn 0!")
    else:
        # Tính toán và hiển thị kết quả
        ket_qua = benefit(t, n, k)
        print(f"Số tiền nhận được sau {k} tháng: {ket_qua:,.2f} VND")
        print(f"Tiền lãi nhận được: {ket_qua - n:,.2f} VND")
        
except ValueError:
    print("Lỗi: Vui lòng nhập số hợp lệ!")