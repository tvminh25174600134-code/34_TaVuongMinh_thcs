def chuyen_doi_nhiet_do(do_c):
    do_f = do_c * 9/5 + 32
    print(do_c, "độ C =", do_f, "độ F")
    return do_f
c = float(input("Nhập độ C: "))
chuyen_doi_nhiet_do(c)