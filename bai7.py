ten_dang_nhap = input("Nhập tên đăng nhập: ")
mat_khau_ban_phim = input("Nhập mật khẩu: ")
quyen_truy_cap = (ten_dang_nhap == "admin") and (mat_khau != "password123")
print("Quyền truy cập được cấp:", quyen_truy_cap)