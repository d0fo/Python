print('Enter integer number:')
n = int(input())
def factorial(m):
    # if m == 1:
    #     return 1
    # else:
    #     return m * mult(m - 1)
    f=1
    for i in range(1,m+1,1):
        f = f*i
    return f
a = []
for i in range(1, n + 1,1):
    a.append(factorial(i))

print(f"Facorials of numbers from 1 to {n} is  {a}")
