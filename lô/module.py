s=str(1223)

found = False
for i in range(len(s) - 1):
    if s[i] == s[i+1]:
        found = True
        break

if found:
    print("true")
else:
    print("false")

        