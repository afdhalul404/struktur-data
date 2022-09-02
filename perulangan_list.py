daftar_peserta = []

while True:
    peserta = str(input("Nama peserta\t:"))
    umur = input("Umur\t\t:")
    gender = input("Jenis Kelamin\t:")
    list_peserta = [peserta, umur, gender]
    daftar_peserta.append(list_peserta)
    print(daftar_peserta)
    for peserta in daftar_peserta:
        print(f"Nama\t: {peserta[0]}")
        print(f"Usia\t: {peserta[1]}")
        print(f"Gender\t: {peserta[2]}")
