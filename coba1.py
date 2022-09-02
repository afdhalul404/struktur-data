'''kumpulan_buku = []
while True:
    judul = input("Masukan judul buku : ")
    penulis = input("Masukan nama penulis : ")
    daftar_buku = [judul, penulis]
    kumpulan_buku.append(daftar_buku)
    print(kumpulan_buku)
    for index, buku in enumerate(kumpulan_buku):
        print(f"| {index+1} | \t{buku[0]}\t | \t{buku[1]}\t |")'''

'''# looping dari list

# for loop
print("For Loop")
kumpulan_angka = [4,3,2,5,6,1]

for angka in kumpulan_angka:
	print(f"angka = {angka}")

peserta = ["ucup","otong","dadang","diding","dudung"]

for nama in peserta:
	print(f"nama = {nama}")

# for loop dan range
print("\nFor Loop dan range")
kumpulan_angka = [10,5,4,2,6,5]

panjang = len(kumpulan_angka)

for i in range(panjang):
	print(f"angka = {kumpulan_angka[i]}")

# while loop
print("\nWhile loop")
kumpulan_angka = [10,5,4,2,6,5]

panjang = len(kumpulan_angka)
i = 0

while i < panjang:
	print(f"angka = {kumpulan_angka[i]}")
	i += 1

# list comprehension
print("\nList Comprehension")
data = ["ucup",1,2,3,"otong"]

[print(f"data={i}") for i in data]

angka = [10,5,4,2,6,5]

angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)

# enumerate
print("\nEnumerate")
data_list = ["ucup",1,2,3,"otong"]

for index,data in enumerate(data_list):
	print(f"index = {index}, data = {data}")'''


kumpulan_angka = [0, 1, 23, 4, 56, 3, 3, 52, 1]

print(kumpulan_angka)
for angka in kumpulan_angka:
    print(angka)

panjang = len(kumpulan_angka)
for angka in range(panjang):
    print(f"angka dengan range: {kumpulan_angka[angka]}")
