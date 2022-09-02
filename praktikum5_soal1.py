daftar_mahasiswa = []

batas = int(input("Masukan Banyak Mahasiswa \t: "))

for i in range(1, batas+1):
    nim = input(f"Masukan Nim mahasiswa ke-{i} \t: E1E1")
    nama = input(f"Masukan Nama mahasiswa ke-{i} \t: ")
    matkul = input(f"Masukan Nama Matakuliah \t: ")
    nilai = int(input(f"Masukan Nilai \t\t\t: "))
    print("\n", "#"*30, "\n")

    if nilai <= 100 and nilai >= 81:
        nilai = "A"
    elif nilai <= 80 and nilai >= 61:
        nilai = "B"
    elif nilai <= 60 and nilai >= 40:
        nilai = "C"
    elif nilai <= 41 and nilai >= 20:
        nilai = "D"
    else:
        nilai = "E"

    kumpulan_mhs = [nim, nama, matkul, nilai]
    daftar_mahasiswa.append(kumpulan_mhs)


print(daftar_mahasiswa)
for mahasiswa in daftar_mahasiswa:
    print(f"Nim \t\t: E1E1{mahasiswa[0]}")
    print(f"Nama \t\t: {mahasiswa[1]}")
    print(f"Mata kuliah \t: {mahasiswa[2]}")
    print(f"Nilai \t\t: {mahasiswa[3]}\n")
