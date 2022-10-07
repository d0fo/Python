import random
def gen_pol(n):
    polinom = ''
    for i in range(n+1):
        if i == 0:
            polinom += str(random.randint(1,101)) + '*x**' + str(n-i)
        elif i == n:
            polinom += '+' + str(random.randint(1,101))
        else:
            polinom += '+' + str(random.randint(1,101)) + '*x**' + str(n-i)
    return polinom
k = int(input())
with open("text.txt", 'w')as t: 
    t.write(gen_pol(k))

