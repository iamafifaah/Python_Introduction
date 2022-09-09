### Operasi Aritmatika

a = 16
b = 5
### penjumlahan
hasil = a + b
print(a,"+",b,"=", hasil)

### pengurangan
hasil = a - b
print(a,"-",b,"=", hasil)

### perkalian
hasil = a * b
print(a,"×",b,"=", hasil)

### pembagian
hasil = a / b
print(a,":",b,"=", hasil, type(hasil)) # otomatis jadi float

### eksponen **
hasil = a ** b
print(a,"^",b,"=", hasil, type(hasil)) 


### modulus %% # merupakan sisa dari pembagian
hasil = a % b
print(a,"%",b,"=", hasil, type(hasil)) 

### floor division //
hasil = a // b
print(a,"//",b,"=", hasil, type(hasil)) 

### Operasi prioritas digunakan otomatis di Python
### kecuali menambahkan kurung secara manual akan didahulukan
x = 3
y = 2
z = 5

hasil = x + y * z
print(x, '+', y ,'*' ,z, '= ', hasil)

print("=== kurung mengambil langkah awal===")
hasil =( x + y) * z
print(x, '+', y ,'*' ,z, '= ', hasil)

'''
Urutan:
            1. Kurung ()
            2. Eksponen **
            3. Perkalian, pembagian dan kawan-kawan *, /, //, %
            4. Penjumlahan dan pengurangan + dan -
'''










