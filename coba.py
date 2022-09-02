'''from copy import copy


daftar_nama = ['afdalul', 'Rahmat']

print(daftar_nama.index("afdalul"))
print(daftar_nama.count("afdalul"))

nama_baru = ['saya']
daftar_nama.extend(nama_baru)
print(hex(id(daftar_nama)))


saya = copy(daftar_nama)
print(hex(id(saya)))


list_angka = [0, 1, 2, 4, 53, 4, 6, 4, 7, 9]

list_angka.sort()
print(f"data diurutkan = {list_angka}")

list_angka.reverse()
print(f"data diurutkan dari atas = {list_angka}")'''

daftar_mhs = []
while True:

    nama = str(input("Masukan Nama\t: "))
    nim = str(input("Masukan Nim\t: "))
    kelas = str(input("Masukan Kelas\t: "))

    data_mhs = [nama, nim, kelas]
    daftar_mhs.append(data_mhs)
    print(daftar_mhs)
