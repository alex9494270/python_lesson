n = input('Введите число')
a = n
d = int(a)
if d >= 0:
    b = n+n
else:
    b = n+str(d*(-1))
e = int(b)
if d >= 0:
    c = n+n+n
else:
    c = n+str(d*(-1))+str(d*(-1))
f = int(c)

print(d+e+f)
