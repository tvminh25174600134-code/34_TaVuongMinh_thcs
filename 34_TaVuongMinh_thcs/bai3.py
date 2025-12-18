def kiem_tra_so_armstrong(n):
    s = str(n)
    tong = 0
    for i in s:
        tong = tong + int(i)**3
    if tong == n:
        print(n, "là số Armstrong")
    else:
        print(n, "không phải số Armstrong")

n = int(input("Nhập số n: "))
kiem_tra_so_armstrong(n)