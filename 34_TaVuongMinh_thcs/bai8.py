# bai8.py
can_nang = float(input("Nhập cân nặng (kg): "))
chieu_cao = float(input("Nhập chiều cao (m): "))
bmi = can_nang / (chieu_cao ** 2)
print("Chỉ số BMI của bạn là: {:.2f}".format(bmi))
