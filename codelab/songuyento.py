n = int(input())
ktra = None
if n ==2:
    ktra = 'Nguyên tố'
elif n == 0 or n ==1:
    ktra = 'Không phải nguyên tố'
else:
    for i in range(2,n):
        if n % i == 0:
            ktra = 'Không khải nguyên tố'
            break
        else:
            ktra = 'Nguyên tố'
print(ktra)