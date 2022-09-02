'''nama_depan = input(str("nama depan : "))
nama_tengah = input(str("nama tengah : "))
nama_belakang = input(str("nama belakang : "))

print(nama_depan, nama_tengah, nama_belakang)

print("panjang nama depan : ", len(nama_depan))
print("panjang nama tengah : ", len(nama_tengah))
print("panjang nama belakang : ", len(nama_belakang))

status = "a" in nama_depan
if (status == True):
    print("huruf a ada pada nama depan")
    # print(nama_depan[1:4])
    print(min(nama_depan))
    print(max(nama_depan))
else:
    print("huruf a tidak ada pada nama depan")'''

######################### MANIPULASI STRING #########################
'''salam = "sist"
apakah_lower = salam.islower()
print(salam + " is lower = " + str(apakah_lower))'''

# isalpha()<-- untuk mengecek semuanya huruf
# isalnum()<-- huruf dan angka
# isdecimal()<-- angka saja
# isspace()<-- spasi,tab,newline In
# istitle()<-- semua kata dimulai dengan huruf besar


'''import datetime
hari_ini = datetime.date.day()
print(hari_ini)'''


#########################  LATIHAN PERCABANGAN #########################
'''angka1 = int(input("Masukan angka 1 : "))
operator = str(input("Pilih Operator (+ - x /) :"))
angka2 = int(input("Masukan angka 2 : "))

if operator == "+":
    hasil = angka1+angka2
    print("hasil penjumlahan ", angka1, " + ", angka2, " = ", hasil)
elif operator == "-":
    hasil = angka1-angka2
    print("hasil penjumlahan ", angka1, " - ", angka2, " = ", hasil)
elif operator == "x":
    hasil = angka1*angka2
    print("hasil penjumlahan ", angka1, " x ", angka2, " = ", hasil)
elif operator == "/":
    hasil = angka1/angka2
    print("hasil penjumlahan ", angka1, " / ", angka2, " = ", hasil)
else:
    print("Operator tidak sesuai, masukan operator dengan benar")

print("selesai")'''


#########################  FOR LOOP #########################
a = int(input('Masukan nilai : '))

# Program 1
for i in range(a):
    for j in range(i+1):
        print("*", end='')
    print('')
print("\n")

'''print("Program 1")
for i in range(a):
    for j in range(i+1):
        print('* ', end='')
    print('')

print("Program 2")
s = a-1
for i in range(a):
    for j in range(s):
        print('* ', end='')
    s -= 1
    print('')

print("Program 3")
s = 2 * a - 2  # for spaces
for i in range(0, a):
    for j in range(0, s):
        print(' ', end='')
    s -= 2
    for j in range(0, i + 1):
        print('* ', end='')
    print('')


print("Program 4")
s = 0  # for spaces
for i in range(0, a):
    for j in range(0, s):
        # print(j, end='')
        print(' ', end='')
    s += 2
    for j in range(0, a):
        print('* ', end='')
    a -= 1
    print('')'''

'''print("Program 5")
s = a - 1  # for spaces
for i in range(0, a):
    for j in range(0, s):
        print(' ', end='')
    s -= 1
    for j in range(0, i + 1):
        print('* ', end='')

    print('')

print('program 6')
s = 0  # for spaces
for i in range(0, a):
    for j in range(0, s):
        print(' ', end='')
    s += 1
    for j in range(0, a):
        print('* ', end='')
    a -= 1
    print('')'''


#########################  WHILE #########################
'''while True:
    print("*"*count)
    count += 1

    if count > a:
        break'''
'''i = 0
while i <= a-1:
    i += 1

    if i % 2 == 0:
        continue
        print(i, ' genap')

    if i % 2 == 1:
        print(i, ' ganjil')'''

# program1
'''string = ""
bar = 1
# Looping Baris
while bar <= a:
    kol = bar

    # Looping Kolom
    while kol > 0:
        string = string + " * "
        kol = kol - 1

    string = string + "\n"
    bar = bar + 1
print(string)'''

# program2
'''string = ""

# Looping Baris
while a >= 0:
    kol = a

    # Looping Kolom
    while kol > 0:
        string = string + " * "
        kol = kol - 1

    string = string + "\n"
    a = a - 1

print(string)'''

# program3
'''string = ""

bar = a
# Looping Baris
while bar >= 0:

    # Looping Kolom Spasi Kosong
    kol = bar
    while kol > 0:
        string = string + "   "
        kol = kol - 1

    # Looping Kolom Bintang
    kanan = 1
    while kanan < (a - (bar-1)):
        string = string + " * "
        kanan = kanan + 1

    string = string + "\n"
    bar = bar - 1

print(string)'''

# program4
'''string = ""
bar = 1

# Looping Baris
while bar <= a:
    # Looping Kolom Spasi Kosong
    kol = bar
    while kol > 1:
        string = string + "   "
        kol = kol - 1

    # Looping Kolom Bintang
    kanan = 0
    while kanan <= (a - bar):
        string = string + " * "
        kanan = kanan + 1

    string = string + "\n"
    bar = bar + 1
print(string)'''

# program5
'''string = ""

bar = a
# Looping Baris
while bar >= 0:
    # Looping Kolom Spasi Kosong
    kol = bar
    while kol > 0:
        string = string + "   "
        kol = kol - 1
    # Looping Kolom Bintang Sisi Kiri
    kiri = 1
    while kiri < (a - (bar-1)):
        string = string + " * "
        kiri = kiri + 1
    # Looping Kolom Bintang Sisi Kanan
    kanan = 1
    while kanan < kiri - 1:
        string = string + " * "
        kanan = kanan + 1

    string = string + "\n\n"
    bar = bar - 1

print(string)'''

# program6
'''string = ""
bar = 1

print("\n")
# Looping Baris
while bar <= a:
    kol = bar
    # Looping Kolom Spasi Kosong
    while kol > 1:
        string = string + "   "
        kol = kol - 1
    # Looping Kolom Bintang Sisi Kiri
    kiri = 0
    while kiri <= (a - bar):
        string = string + " * "
        kiri = kiri + 1
    # Looping Kolom Bintang Sisi Kanan
    kanan = kiri
    while kanan > 1:
        string = string + " * "
        kanan = kanan - 1

    string = string + "\n\n"
    bar = bar + 1
print(string)'''

# program7
'''string = ""

bar = a
# Looping Baris
while bar >= 0:
    # Looping Kolom Spasi Kosong
    kol = bar
    while kol > 0:
        string = string + "   "
        kol = kol - 1
    # Looping Kolom Bintang Sisi Kiri
    kiri = 1
    while kiri < (a - (bar-1)):
        string = string + " * "
        kiri = kiri + 1
    # Looping Kolom Bintang Sisi Kanan
    kanan = 1
    while kanan < kiri - 1:
        string = string + " * "
        kanan = kanan + 1

    string = string + "\n\n"
    bar = bar - 1

bar = 1
# Looping Baris
while bar <= a:
    kol = bar+1
    # Looping Kolom Spasi Kosong
    while kol > 1:
        string = string + "   "
        kol = kol - 1
    # Looping Kolom Bintang Sisi Kiri
    kiri = 0
    while kiri < (a - bar):
        string = string + " * "
        kiri = kiri + 1
    # Looping Kolom Bintang Sisi Kanan
    kanan = kiri
    while kanan > 1:
        string = string + " * "
        kanan = kanan - 1

    string = string + "\n\n"
    bar = bar + 1
print(string)'''


'''peserta1 = ["Afdhalul", 2002, 'Islam']
peserta2 = ["Budi", 2003, 'Kristen']
peserta3 = ["Agus", 2004, 'Hindu']

daftar_peserta = [peserta1, peserta2, peserta3]

for peserta in daftar_peserta:
    print(f"Nama : {peserta[0]}")
    print(f"Tahun : {peserta[1]}")
    print(f"Agama: {peserta[2]}\n")
'''
'''daftar_peserta = []
while True:
    nama = str(input("Masukan Nama: "))
    tahun = str(input("Masukan Tahun: "))
    agama = str(input("Masukan Agama: "))

    data_peserta = [nama, tahun, agama]
    daftar_peserta.append(data_peserta)

    lanjut = input("\nApakah Lanjut (y/t): ")
    if lanjut == 't':
        break

for peserta in daftar_peserta:
    print(f"nama : {peserta[0]}")
    print(f"tahun : {peserta[1]}")
    print(f"agama : {peserta[2]}\n")
'''
