nam = int(input("Nhập một năm: "))
nam_nhuan = (nam % 400 == 0) or (nam % 4 == 0) and (nam % 100 !=0)
print("Năm", nam, "là năm nhuận:", nam_nhuan)
print("Năm", nam, "không phải là năm nhuận:", not la_nam_nhuan)