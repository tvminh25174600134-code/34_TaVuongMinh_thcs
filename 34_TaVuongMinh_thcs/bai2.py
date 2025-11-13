# bai2.py
tong_keo = int(input("Nhập tổng số kẹo: "))
so_hoc_sinh = int(input("Nhập số học sinh: "))

keo_moi_ban = tong_keo // so_hoc_sinh
keo_thua = tong_keo % so_hoc_sinh

print("Mỗi học sinh nhận được: {} kẹo".format(keo_moi_ban))
print("Số kẹo còn thừa: {}".format(keo_thua))
