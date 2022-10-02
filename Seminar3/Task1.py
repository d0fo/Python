m = [2, 3, 5, 9, 3, 1]
n = []
for i in range(len(m)):
    if i%2!=0:
        n.append(m[i])
print(n)