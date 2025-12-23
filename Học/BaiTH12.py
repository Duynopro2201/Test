chuoi = list(map(int, input("Nhập danh sách số (cách nhau bởi dấu cách): ").split()))
max_count=0
ki_tu_nhat= None
for x in chuoi:
    if chuoi.count(x) > max_count:
        max_conut = chuoi.count(x)
        ki_tu_nhat = x
    print( ki_tu_nhat )
    print( max_count )