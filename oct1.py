a = "11"
b = "1"
res = ""
c = 0

if len(a) > len(b):
    b[::-1] += "0"
elif len(b) > len(a):
    a

for i,v in enumerate(a[::-1]):
    if i <= len(b)-1 and int(v) + int(b[::-1][i]) == 1 and c == 0:
        res += "1"
        print(int(v) + int(b[::-1][i]), 1)
    elif i == len(a)-1 and int(v) + int(b[::-1][i]) == 1 and c == 1:
        print(int(v) + int(b[::-1][i]), 2)
        res += "1"
    elif i <= len(b)-1 and int(v) + int(b[::-1][i]) == 1 and c == 1:
        res += "0"
        print(int(v) + int(b[::-1][i]), 3)
    elif i <= len(b)-1 and int(v) + int(b[::-1][i]) >= 2:
        print(int(v) + int(b[::-1][i]), 4) 
        res += "0"
        c += 1

print(res[::-1])
