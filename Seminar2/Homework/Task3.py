print('Enter integer number:')
n = int(input())
a=[]
for i in range(1,n+1,1):
    a.append((i+1/i)**i)
print(a)
print(sum(a))