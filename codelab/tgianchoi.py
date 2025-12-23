n = int(input())
ds = {}

for i in range(n):
    ma = input()
    ten = input()
    tgian_vao = list(map(int, input().split(':')))
    tgian_ra = list(map(int, input().split(':')))

    tong_tgian = (tgian_ra[0]*60 + tgian_ra[1]) - (tgian_vao[0]*60 + tgian_vao[1])
    tong_gio = tong_tgian // 60
    tong_phut = tong_tgian % 60

    ds[ma] = [ten, tong_phut, tong_gio, tong_tgian]

# sắp xếp theo tổng thời gian giảm dần
dsm = sorted(ds.items(), key=lambda x: x[1][3], reverse=True)

# in kết quả
for ma, info in dsm:
    ten = info[0]
    phut = info[1]
    gio = info[2]
    print(ma, ten, gio, 'gio', phut, 'phut')
