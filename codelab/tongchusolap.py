'''
Tính digital root của một số nguyên dương n.
(Digital root là tổng các chữ số của n, nếu kết quả có nhiều hơn 1 chữ số thì tiếp tục tính tổng các chữ số đó cho đến khi được số có một chữ số)

Input: một số nguyên dương n
Output: số nguyên một chữ số là digital root
Ví dụ

n = 38 → 3 + 8 = 11 → 1 + 1 = 2 → output = 2
Ràng buộc

Sử dụng vòng lặp và rẽ nhánh.
'''
so = int(input('Nhập số:'))
if so <= 0:
    print(so)
else:
    while True:
        chuoi = []
        tong = 0
        chuoi += str(so)
        if len(chuoi) > 1:
            for i in chuoi:
                tong += int(i)
        else:
            break
        so = tong
print(so)
