f = open("duy.txt", "r", encoding="utf-8")
for line in f:
    print(line.strip())   # loại bỏ ký tự xuống dòng
f.close()