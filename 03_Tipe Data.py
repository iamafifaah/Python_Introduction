## Tipe Data
    # macam-macam data yang bisa digunakan di Python
    # Tipe angka satuan / integer
intg = 1
print("data : ", intg, ", bertipe : ", type(intg))

    # Tipe data float / angka desimal
floatt = 125.5
print("data : ", floatt, ", bertipe : ", type(floatt))

    # Tipe data string / huruf
stringg = "i'm okay"
print("data : ", stringg, ", bertipe : ", type(stringg))

    # Tipe data biner (true/false) atau boolean
boolean = True
print("data : ", boolean, ", bertipe : ", type(boolean))

  # Tipe data biner (true/false) atau boolean
boolean2 = False
print("data : ", boolean2, ", bertipe : ", type(boolean2))

    # Tipe data khusus
# bilangan kompleks
data_kompleks = complex(5,6)
print("data : ", data_kompleks, ", bertipe : ", type(data_kompleks))

    # Tipe data dari bahasa C
# import dulu packages nya
from ctypes import c_double, c_char, c_float, c_long
data_c_double = c_double(10.5)
print("data : ", data_c_double, ", bertipe : ", type(data_c_double))