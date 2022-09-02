from itertools import count


kalimat = str(input("masukan teks: "))
print(f"kalimat {kalimat} berisi: ")

for kata in kalimat:
    jumlah = kalimat.count(kata)
    print(kata, " = ", jumlah)
