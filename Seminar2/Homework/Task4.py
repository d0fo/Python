import random
print('enter the number:')
n = int(input())
m=[]
for i in range(-n, n+1, 1):
    m.append(random.randint(-n,n))
print(m)
print('Enter amount of positions:')
a = int(input())
if a<=2*n+1:
    multi = 1
    for j in range(1, a+1, 1):
        print(f'enter {j} position')
        multi = multi*m[int(input())]
    print(multi)
else:
    print('Too much positions')
