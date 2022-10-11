field = ['1','2','3',
         '4','5','6',
         '7','8','9']
for i in range(0,len(field),3):
    print(field[i],field[i+1],field[i+2])
field[int(input())-1] = 'X'
for i in range(0,len(field),3):
    print(field[i],field[i+1],field[i+2])
field[int(input())-1] = '0'
for i in range(0,len(field),3):
    print(field[i],field[i+1],field[i+2])
if field[1]==0:
    print('end')
