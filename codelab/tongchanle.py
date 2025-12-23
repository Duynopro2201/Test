n = int(input())
chuoi = []
tong_chan = 0
tong_le =0
chuoi += str(n)
for j in chuoi:
    if int(j) % 2 == 0:
            tong_chan += 1
    else:
            tong_le += 1
output = []
output.append(tong_chan)
output.append(tong_le)
print(output)