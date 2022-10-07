from sympy import true
import sympy
n = int(input())
m = []
for i in range(1,n+1):
    if n%i == 0:
        if sympy.isprime(i)==true:
            m.append(i)
        
print(m)