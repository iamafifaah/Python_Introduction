### Operasi Bitwise atau Biner atau Binary
### operasi yang dilakukan pada masing-masing bit

a = 9
b = 5

### bitwise OR (|)
c = a | b
print("====OR====")
print("nilai :", a, "  , binary :", format(a, '08b'))
print("nilai :", b, "  , binary :", format(b, '08b'))
print("nilai :", c, " , binary :", format(c, '08b'))

### bitwise AND (&)
c = a & b
print("====AND====")
print("nilai :", a, " , binary :", format(a, '08b'))
print("nilai :", b, " , binary :", format(b, '08b'))
print("nilai :", c, " , binary :", format(c, '08b'))

### bitwise XOR (^)
c = a ^ b
print("====XOR====")
print("nilai :", a, "  , binary :", format(a, '08b'))
print("nilai :", b, "  , binary :", format(b, '08b'))
print("nilai :", c, " , binary :", format(c, '08b'))

### bitwise NOT (~)
c = ~a ## bilangan biner akan di mirrorkan jika dilakukan operasi NOT
# dengan ketentuan mirror 1 = -2, 2 = -3, dst karena nilai 0 tidak memiliki negatif dan masuk 
# ke rentang positif
print("====NOT====")
print("nilai :", c, " , binary :", format(c, '08b'))


#### jika ingin flip angka biner, trik dengan melakukan XOR dengan biner 11111111
print("=====(^)=====")
d = 0b00001001
e = 0b11111111
print("nilai :", e^d, " , binary : ", format(e^d, '08b'))

### Shifting digunakan untuk menggeser
### shift right atau shift left

### Shift right (>>)
print("==== Shift Right (>>) ====")
c = a >> 2
print("nilai :", a, " , binary : ", format(a, '08b'))
print("nilai :", c, " , binary : ", format(c, '08b'))

### Shift left (<<)
print("==== Shift Left (<<) ====")
c = a << 2
print("nilai :", a, "  , binary : ", format(a, '08b'))
print("nilai :", c, " , binary : ", format(c, '08b'))