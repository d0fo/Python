print('enter X:')
x = int(input())
print('enter Y:')
y = int(input())
if x > 0 and y > 0:
    print('1 quarter')
elif x < 0 and y > 0:
    print ('2 quarter')
elif x < 0 and y < 0:
    print ('3 quarter')
elif x > 0 and y < 0:
    print ('4 quarter')