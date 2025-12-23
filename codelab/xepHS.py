n = int(input())
ds = {}
for i in range(1,n+1):
    msv = f'HS0{str(i)}'
    ten = input()
    diem = list(map(int, input().split()))
    tong = sum(diem[0:2])*2 + sum(diem[2:10])
    dtb = tong / 12
    hanh_kiem = None
    if 0 <= dtb < 5:
        hanh_kiem = 'YEU'
    elif 5 <= dtb < 7:
        hanh_kiem = 'TB'
    elif 7 <= dtb < 8:
        hanh_kiem = 'KHA'
    elif 8 <= dtb < 9:
        hanh_kiem = 'GIOI'
    elif 9 <= dtb <= 10:
        hanh_kiem = 'XUAT SAC'
    else:
        hanh_kiem = 'KHONG HOP LE'
    ds[msv] = [ten,dtb,hanh_kiem]
dsm = dict(sorted(ds.items(), key = lambda x:x[1][1], reverse = True))
for i in dsm:
    ten, dtb, hanh_kiem = dsm[i]
    print(i,ten,f'{dtb:.1f}',hanh_kiem)