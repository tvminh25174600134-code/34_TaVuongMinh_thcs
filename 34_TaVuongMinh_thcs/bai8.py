def tim_so_le_lon_nhat(a, b, c):
    lon_nhat = -1
    if a % 2 != 0:
        lon_nhat = a
    if b % 2 != 0 and b > lon_nhat:
        lon_nhat = b
    if c % 2 != 0 and c > lon_nhat:
        lon_nhat = c
    print("Số lẻ lớn nhất là:", lon_nhat)

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
tim_so_le_lon_nhat(a, b, c)