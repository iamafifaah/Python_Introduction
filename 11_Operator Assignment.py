### Operasi yang dapat dilakukan dengan penyingkatan
### Operasi yang ditambah dengan assignment
### Operasi Aritmatika
print("===Operasi Aritmatika===")
a = 5 ### adalah assignment
print("nilai a  =",a)

a = a + 1
print("nilai a+1=",a)

# Penjumlahan
a += 1
print("nilai a+=1",a)

# Pengurangan
a -= 2
print("nilai a-=2",a)

# Perkalian
a *= 5
print("nilai a*=5",a)

# Pembagian
a /= 5
print("nilai a/=5",a)

# Modulus
b = 10
b %= 3
print("nilai b%=3",b)

# Left Division, dibulatkan ke bawah
b = 10
b //= 3
print("nilai b%=3",b)

### Pangkat
a = 5 ### adalah assignment
print("nilai a  =",a)
a **= 3 
print("nilai a**=3",a)

# Operasi Bitwise
print("===Operasi Bitwise===")
print("===Or | ===")

c = True
print("nilai c  =",c)

### Operasi Bitwise Or |
c = True
c |= False
print("nilai c  =",c)

c = False
c |= True
print("nilai c  =",c)

c = True
c |= True
print("nilai c  =",c)

c = False
c |= False
print("nilai c  =",c)

print("===And & ===")
c = True
c &= False
print("nilai c  =",c)

c = False
c &= True
print("nilai c  =",c)

c = True
c &= True
print("nilai c  =",c)

c = False
c &= False
print("nilai c  =",c)

print("===Xor ^ ===")
c = True
c ^= False
print("nilai c  =",c)

c = False
c ^= True
print("nilai c  =",c)

c = True
c ^= True
print("nilai c  =",c)

c = False
c ^= False
print("nilai c  =",c)

### Shift Right and Left in Binary

d = 0b0100
print("nilai d =",d)
print("nilai d =", format(d, '04b'))

## Shift Right
d >>= 2
print("nilai d =",d)
print("nilai d =", format(d, '04b'))

## Shift Left
d <<= 1
print("nilai d =",d)
print("nilai d =", format(d, '04b'))


########### END ###########
