a = [1, 2, 3, 3, 4, 4, 5]
b = [str(i) for i in a]
print(b)
c = ''
for i in b:
    c += i
print(c)
res=[]
for i in c:
    if c.count(i) == 1:
        res.append(int(i))
print(res)