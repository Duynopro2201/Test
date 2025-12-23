sv = {}
def nhap():
        Hoten = input("Nhap ho ten")
        try:
            diem1 = int(input("Nhap diem1: "))
            diem1 *= 3
            diem2 = int(input("Nhap diem2: "))
            diem2 *= 3
            diem3 = int(input('Nhập điểm 3:'))
            diem3 *= 2
            if 0 <= diem1 <= 30 and 0 <= diem2 <= 30 and 0 <= diem3 <= 20:
                print("Da nhap thanh cong")
                sv[Hoten] = sum((diem1, diem2, diem3))/8

            else:
                print("Diem phai lon hon 0 va nho hon 10")
        except:
            print("Nhap lai: ")
msv = 0
so = int(input("nhap so SV: "))
for i in range(1, so+1):
    msv += 1
    print(f"SV{msv}")
    nhap()
    
print(sv)