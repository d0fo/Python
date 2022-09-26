print('enter X:')
x = int(input())
print('enter Y:')
y = int(input())
print('enter Z:')
z = int(input())
if (not (x or y or z )) == (not x and not y and not z):
    print('¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z is true')
else:
    print('¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z is false')