a = int(input("Masukan jumlah angka = "))
daftar = []
for i in range(1, a+1):
    b = int(input(f"Masukan nilai ke-{i} = "))
    daftar.append(b)


jml = len(daftar)

##### Nilai Tertinggi #####
maks = daftar[0]
for j in range(0, jml):
    if daftar[jml-j-1] > maks:
        maks = daftar[jml-j-1]
print(f"Nilai tertinggi\t= {maks}")

##### Nilai Terendah #####
minimal = daftar[0]
for j in range(0, jml):
    if daftar[jml-j-1] < minimal:
        minimal = daftar[jml-j-1]
print(f"Nilai terendah \t= {minimal}")

##### Rata-Rata #####
total = 0
for j in range(jml):
    total += daftar[jml-j-1]
print(f"total = {total}")
rata2 = total/jml
print(f"Rata-rata \t= {rata2}")
