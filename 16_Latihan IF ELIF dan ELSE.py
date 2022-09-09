angka1 = int(input('masukkan angka :'))
angka2 = int(input('masukkan angka :'))
operator = input("masukkan operator")
if angka1 == 4 and angka2 == 5 and operator == "+" :
    print(angka1,"+", angka2, "=", angka1+angka2)
elif operator == "*":
    hasil = angka1 * angka2
    print(angka1,"⨉",angka2, "=", hasil)
else:
    print("input salah!")
