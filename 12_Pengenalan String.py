from regex import R


data = "ini adalah string"
print(data)
print(type(data))

# Cara membuat string

'''
    1. Dengan menggunakan single quote '...'
    2. Dengan menggunakan double quote "..."
'''

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

print('"Halo, apa kabar?"')
print("'Halo, apa kabar?'")
print("ini adalah hari jum'at")

# 2. Menggunakan tanda \

# membuat tanda ' menjadi string
print('mari sholat jum\'at')
print('g\'day, isn\'t it?')

# Backlash
print("C:\\user\\Refal")

# Tab
print("Refal\tHady, spasi jadi jauh")
print("Refal\t\t\tHady, spasi banyak jadi makin jauh")

# backspace
print("Refal \bHady, jadi dekat jaraknya")

# New Line untuk deteksi baris baru
print("baris pertama.\nbaris kedua.") #LF -> line fit unix, mac os, linux
print("baris pertama.\rbaris kedua.") # CR -> carriage return commodore, acorn, lisp
print("baris pertama.\r\nbaris kedua.") # CRLF  -> line feed carriage return dipakai windows

# 3. String Literal atau raw

# hati-hati
print('C:\new folder')
print('C:\\new folder')

# menggunakan raw string 
print(r'C:\new folder') ### semua tanda jadi string

### multi line literal string
print(
    '''
    Nama: Apipah
    Kelas : 4 SMA
    '''
)

### menggabungkan multiline literal string dan raw
print(
    r'''
    Nama: Apipah
    Kelas : 4 SMA
    Website : www.apipah.com\newID
    '''
)