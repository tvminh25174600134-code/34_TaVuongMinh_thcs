# bai5.py
tien_gui = float(input("Nhập số tiền gửi ban đầu (VND): "))
lai_suat = float(input("Nhập lãi suất hàng năm (%): "))
so_nam = float(input("Nhập số năm gửi: "))
tien_lai = tien_gui * lai_suat / 100 * so_nam
tong_tien = tien_gui + tien_lai
print("Tiền lãi nhận được: {:.2f} VND".format(tien_lai))
print("Tổng tiền sau {:.0f} năm: {:.2f} VND".format(so_nam, tong_tien))
