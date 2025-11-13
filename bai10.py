# bai10.py
luong_co_ban = float(input("Nhập lương cơ bản (VND): "))
so_ngay_lam = int(input("Nhập số ngày làm việc: "))
luong_thang = luong_co_ban / 22 * so_ngay_lam
phu_cap = luong_thang * 0.1   
thue = luong_thang * 0.05   
thuc_lanh = luong_thang + phu_cap - thue
print("Tổng lương thực nhận: {:.2f} VND".format(thuc_lanh))
