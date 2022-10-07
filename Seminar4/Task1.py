import math
a = 0.001
b = str(a)
fif = b.find('.')
c = b[fif+1::]
print(round(math.pi, len(c)))
