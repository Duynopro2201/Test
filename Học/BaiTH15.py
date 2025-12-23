vanban=input('Nhập văn bản bạn cần phân tích:').lower()
for dau in ',.?!':
    vanban=vanban.replace(dau,'')
work=vanban.split()

dem_tu={}
for tu in work:
    if tu in dem_tu:
        dem_tu[tu] += 1
    else :
        dem_tu[tu]=1
sapxep=sorted ( dem_tu.items(), key=lambda x: x[1], reverse=True )


for tu,so_lan in sapxep:
    print(tu,':',so_lan)
    