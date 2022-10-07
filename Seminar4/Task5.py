import sympy
x = sympy.Symbol('x')
with open("text1.txt", 'r') as t1:
    a = t1.read()
print (a)
with open("text2.txt", 'r') as t2:
    b = t2.read()
print(b)
c = sympy.simplify(a+'+'+b)
with open("text.txt", 'w') as t:
    t.write(str(c))
print(c)