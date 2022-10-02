m = [2, 3, 4, 5, 6]
n = []
if len(m)%2==0:
    for i in range(len(m)//2):
        n.append(m[i]*m[len(m)-1-i])
else:
     for i in range(len(m)//2+1):
        n.append(m[i]*m[len(m)-1-i])
print(n)