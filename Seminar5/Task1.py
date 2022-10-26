import random
a = 100
print('There is 2021 candies on the table')
print('You can take between 1 and 28 candies')
while a>0:
    d=0
    if a>0:
        print('Enter the number of candies you want to take')
        b = int(input())
        a = a - b
        print(f'{a} candies left on the table')
        d =0 
    if a == 0 and d == 0:
        print('You win')    
    if a > 28:
        c = random.randint(1,28)
        a = a - c
        print(f'Robot took {c} candies')
        print(f'{a} candies left on the table')
        d = 1
    if 0<a<28 and d == 0:
        c = random.randint(1,a+1)
        a = a - c
        print(f'Robot took {c} candies')
        print(f'{a} candies left on the table')
        d = 1
    if a == 0 and d == 1:
        print('Robot win') 


