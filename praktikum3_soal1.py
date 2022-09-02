kali = int(input("Masukan Perkalian   : "))
mulai = int(input("Masukan nilai awal  : "))
akhir = int(input("Masukan nilai akhir : "))

i = mulai
while i <= akhir:
    hasil = kali*i
    print(f"{i} x {kali} = {hasil}")
    i += 1
