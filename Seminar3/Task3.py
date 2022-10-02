m0 = [1.1, 1.2, 3.1, 5, 10.01]
m = [str(i) for i in m0]
a = []
for i in range(len(m)):
   x = m[i].split('.')
   a.append(round(m0[i]-int(x[0]), 2))
max = a[0]
min = a[0]
for i in a:
    if i > max:
        max = i
    elif i < min and i != 0:
        min = i
print(max, min)
print(max-min)

