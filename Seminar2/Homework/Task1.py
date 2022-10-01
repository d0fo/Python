print('Enter real number:')
a = float(input())
b = str(a)
x = b.split(".") 
n = int(x[0]) 
m = int(x[1]) 
mult = 1
while (n != 0): 
    mult = mult * (n % 10)
    n = n // 10
while (m != 0): 
    mult = mult * (m % 10)
    m = m // 10
print('Number digits multiplicaton is:', mult)
