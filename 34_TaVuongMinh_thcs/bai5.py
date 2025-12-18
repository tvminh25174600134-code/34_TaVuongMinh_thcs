def kiem_tra_so_doi_xung(n):
    s = str(n)
    s_dao = ""
    for i in range(len(s)-1, -1, -1):
        s_dao = s_dao + s[i]
    if s == s_dao:
        print(n, "là số đối xứng")
    else:
        print(n, "không phải số đối xứng")

n = int(input("Nhập số n: "))
kiem_tra_so_doi_xung(n)
