n = int(input())
each_student = []
all_students = 0
for i in range(n):
    diem = list(map(int, input().split()))
    tong = sum(diem)
    each_student.append(tong)
    print(tong)
    all_students += tong
s = (all_students / (2*(n-1)))
print(s)
can = []
if n == 2:
    for i in each_student:
        diem_rieng = i / 2
        can.append(round(diem_rieng))
else:
    for i in each_student:
        diem_rieng = (i - s) / (n - 2)
        can.append(round(diem_rieng))
print(*can)
        