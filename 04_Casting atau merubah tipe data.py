#casting mengubah satu tipe data ke tipe data lain
# tipe data: int, float, str, bool
# Data Integer
# int ke float
import string
print("=====Integer=====")
data_int = 9;
print("data = ", data_int, ", type = ", type(data_int))

# int ke float
data_float = float(data_int)
print("data = ", data_float, ", type = ", type(data_float))

# int ke string
data_string = str(data_int)
print("data = ", data_string, ", type = ", type(data_string))

# int ke boolean
data_bool = bool(data_int)
print("data = ", data_bool, ", type = ", type(data_bool))
data_int2 = 0; # kalau int 0 boolean akan bernilai false, selain itu True
data_bool2 = bool(data_int2)
print("data = ", data_bool2, ", type = ", type(data_bool2))

# Data Float
print("=====Float=====")
data_float = 9.5;
print("data = ", data_float, ", type = ", type(data_float))

# float ke integer
data_int = int(data_float)
print("data = ", data_int, ", type = ", type(data_int))

# float ke string dibulatkan ke bawah
data_string = str(data_float)
print("data = ", data_string, ", type = ", type(data_string))

# float ke boolean
data_bool = bool(data_float)
print("data = ", data_bool, ", type = ", type(data_bool))
data_int2 = 0; # kalau float 0 boolean akan bernilai false
data_bool2 = bool(data_int2)
print("data = ", data_bool2, ", type = ", type(data_bool2))

# Data Boolean
print("=====Boolean jika True=====")
data_bool = True;
print("data = ", data_bool, ", type = ", type(data_bool))
# bool ke integer akan jadi 1
data_int = int(data_bool)
print("data = ", data_int, ", type = ", type(data_int))

# bool ke string jadi teks
data_string = str(data_bool)
print("data = ", data_string, ", type = ", type(data_string))

# bool ke float
data_float = float(data_bool)
print("data = ", data_float, ", type = ", type(data_float))

print("=====Boolean jika False=====")
data_bool = False;
print("data = ", data_bool, ", type = ", type(data_bool))
# bool ke integer akan jadi 0
data_int = int(data_bool)
print("data = ", data_int, ", type = ", type(data_int))

# bool ke string jadi teks
data_string = str(data_bool)
print("data = ", data_string, ", type = ", type(data_string))

# bool ke float
data_float = float(data_bool)
print("data = ", data_float, ", type = ", type(data_float))

print("=====String jika Angka=====")
data_str2 = "50"; # data berupa huruf/string tidak bisa diubah 
# menjadi integer, float, maupun boolean kecuali berupa angka
print("data = ", data_str2, ", type = ", type(data_str2))

# string ke integer
data_int = int(data_str2)
print("data = ", data_int, ", type = ", type(data_int))

# string ke boolean
data_bool = bool(data_str2)
print("data = ", data_bool, ", type = ", type(data_bool))

# string ke float
data_float = float(data_str2)
print("data = ", data_float, ", type = ", type(data_float))

print("=====String jika Nol / 0 atau False =====")
data_str2 = "0"; # data berupa huruf/string tidak bisa diubah 
# menjadi integer, float, maupun boolean kecuali berupa angka
print("data = ", data_str2, ", type = ", type(data_str2))

# string ke integer
data_int = int(data_str2)
print("data = ", data_int, ", type = ", type(data_int))

# string ke boolean
print("====Maka, Boolean tetap true====")
data_bool = bool(data_str2)
print("data = ", data_bool, ", type = ", type(data_bool))
print("==Boolean bernilai false jika string kosong==")
# string ke float
data_float = float(data_str2)
print("data = ", data_float, ", type = ", type(data_float))

# print("=====String=====") akan error jika di running
# data_str = "Refal Hady?"; # data berupa huruf/string tidak bisa diubah 
# menjadi integer, float, maupun boolean kecuali berupa angka
# print("data = ", data_str, ", type = ", type(data_str))

# string ke integer
# data_int = int(data_str)
# print("data = ", data_int, ", type = ", type(data_int))

# string ke boolean
# data_bool = bool(data_str)
# print("data = ", data_bool, ", type = ", type(data_bool))

# string ke float
# data_float = float(data_str)
# print("data = ", data_float, ", type = ", type(data_float))