def can_ktra(so_can_ktra,a):
    tong = 0
    while so_can_ktra != 0 : 
        tung_so = so_can_ktra % 10
        so_can_ktra = so_can_ktra // 10
        tong += tung_so**a
    return tong
a = 0   
so_ktra = int(input())
for i in range(1,10):
    
    if can_ktra(so_ktra,i) == so_ktra:
        a += 1
       
if a > 0:
    print('Armstrong')
else:
    print('Không phải là Armstrong')