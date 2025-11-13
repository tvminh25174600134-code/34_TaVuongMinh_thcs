# bai1.py
gia = float(input("Nhập giá sản phẩm: "))
so_luong = int(input("Nhập số lượng mua: "))
tong = gia * so_luong
vat = tong * 0.1
tong_tien = tong + vat
print("Tổng tiền phải trả: {:.2f} VND".format(tong_tien))
