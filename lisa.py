kumpulan_nama = []

n = int(input("Masukan jumlah nama :"))

for i in range(1, n+1):
    n += 1
    nama = str(input(f"Masukan Nama ke {i} : "))
    kumpulan_nama.append(nama)

for enter in kumpulan_nama:
    data = enter.split()

    for d in data:
        print(d[0], end="")
    print("")

# Program 2
'''from audioop import reverse


kumpulan_angka = []
batas = int(input("Masukan batas : "))

for i in range(1, batas+1):
    batas += 1
    angka = str(input(f"Masukan Angka ke {i} : "))
    kumpulan_angka.append(angka)

print(kumpulan_angka)
kumpulan_angka.reverse()
print(kumpulan_angka)
if len(kumpulan_angka) != kumpulan_angka.reverse():
    print("True")
else:
    print("True")'''
