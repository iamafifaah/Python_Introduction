### Operasi Logika atau Boolean

### not, or, and, xor
### Output berupa True atau False
from operator import xor
from sympy import Xor


print("===Not===")
a = True
c = True
d = not a
b = not c
print('data a = ', a)
print('data c = ', c)
print('data d = ', d)
print('data b = ', b)

print("===Or===")

a = True
b = True
c = a or b
print(a, 'or' , b, '=', c)

a = True
b = False
c = a or b
print(a, 'or' , b, '=', c)

a = False
b = True
c = a or b
print(a, 'or' , b, '=', c)

a = False
b = False
c = a or b
print(a, 'or' , b, '=', c)

print("===AND===")

a = True
b = True
c = a and b
print(a, 'and' , b, '=', c)

a = True
b = False
c = a and b
print(a, 'and' , b, '=', c)

a = False
b = True
c = a and b
print(a, 'and' , b, '=', c)

a = False
b = False
c = a and b
print(a, 'and' , b, '=', c)

print("===XOR===")

a = True
b = True
c = a ^ b
print(a, 'xor' , b, '=', c)

a = True
b = False
c = a ^ b
print(a, 'xor' , b, '=', c)

a = False
b = True
c = a ^ b
print(a, 'xor' , b, '=', c)

a = False
b = False
c = a ^ b
print(a, 'xor' , b, '=', c)