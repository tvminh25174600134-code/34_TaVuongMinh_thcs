so_kwh = int(input("Nhập số kWh điện đã tiêu thụ: "))
bac1 = min(so_kwh, 200)
bac2 = min(min(so_kwh - 100, 0), 200)
bac3 = min(max(so_kwh - 200, 0), 200)
gia_bac1 = 1678
gia_bac2 = 1734
gia_bac3 = 2014
tong_tien = bac1 * gia_bac1 + bac2 * gia_bac2 + bac3 * gia_bac3
print("Tổng số tiền điện phải trả là:", tong_tien, "VNĐ")