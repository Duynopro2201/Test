n = int(input())
fibonacci = 0
chuoi = [0,1]
st1 = 0
st2 = 1
st3 = 0
if n <= 0:
    print('Không hợp lệ')
else:
    while fibonacci <= n:
        st3 = int(st1) + st2
        st1 = st2
        st2 = st3
        chuoi.append(st3)
print(*chuoi)