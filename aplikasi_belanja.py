daftar_nama = []


while True:
    nama = input("Masukan nama: ")
    list_nama = [nama]
    daftar_nama.append(list_nama)

    # keluar
    keluar = input("lanjut/Tidak (y/t)")
    if keluar == 't':
        break

new_list = [x for x in daftar_nama if "a" in x]
print(new_list)
print(daftar_nama)
