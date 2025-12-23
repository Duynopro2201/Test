def tan_suat(ds):
    ds_moi = []
    lan_xuat_hien = {}
    for i in ds:
        if i not in ds_moi:
            ds_moi.append(i)
            lan_xuat_hien[i] = ds.count(i)
    for i in lan_xuat_hien:
        print(f"Số lần '{i}' xuất hiện là: {lan_xuat_hien[i]}")
        
n = input()             
ds = list(map(str, n.split()))
tan_suat(ds)