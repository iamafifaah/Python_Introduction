# Setiap hasil dari hasil komparasi adalah True atau False

### >,<, >=,<=,==,!=, is, is not
### bekerja pada syntax literal

a = 4
b = 2
### lebih besar dari >
print("=== Lebih Besar Dari > ")
hasil = a > 3
print(a, '>', 3, '=', hasil)
hasil = b > 3
print(b, '>', 3, '=', hasil)
hasil = b > 2 # 2 bukan > 2, maka false, jika 2.1 > 2 maka true
print(b, '>', 2, '=', hasil)

# Kurang Dari
print("=== Kurang Dari < ")
hasil = a < 3
print(a, '<', 3, '=', hasil)
hasil = b < 3
print(b, '<', 3, '=', hasil)
hasil = b < 2 
print(b, '<', 2, '=', hasil)

# Lebih Dari Sama Dengan 
print("=== Lebih dari sama dengan >=")
hasil = a >= 3
print(a, '>=', 3, '=', hasil)
hasil = b >= 3
print(b, '>=', 3, '=', hasil)
hasil = b >= 2 
print(b, '>=', 2, '=', hasil)

# Kurang Dari Sama Dengan 
print("=== Kurang dari sama dengan <=")
hasil = a <= 3
print(a, '<=', 3, '=', hasil)
hasil = b <= 3
print(b, '<=', 3, '=', hasil)
hasil = b <= 2 
print(b, '<=', 2, '=', hasil)

# Sama Dengan == membandingkan apakah nilainya sama 
print("=== sama dengan ==")
hasil = a == 4
print(a, '==', 4, '=', hasil)
hasil = b == 4
print(b, '==', 4, '=', hasil)
hasil = b == 2 
print(b, '==', 2, '=', hasil)

# Tidak Sama Dengan != membandingkan 
print("=== tidak sama dengan !=")
hasil = a != 4
print(a, '!=', 4, '=', hasil)
hasil = b != 4
print(b, '!=', 4, '=', hasil)
hasil = b != 2 
print(b, '!=', 2, '=', hasil)

### is digunakan untuk membandingkan object, 
# tidak bisa untuk literal, True dan False karena beda id
print("=== is dan is not ===")
a = 4
b = 4
c = a is b
print("a = 4")
print("b = 4")
print("a is b =", c)

print("----------------------")
a = 3
b = 4
c = a is b
print("a = 3")
print("b = 4")
print("a is b =", c)

print("----------------------")
a = 4
b = 4
c = a is not b
print("a = 4")
print("b = 4")
print("a is not b =", c)

print("----------------------")
a = 3
b = 4
c = a is not b
print("a = 3")
print("b = 4")
print("a is not b =", c)
print("----------------------")