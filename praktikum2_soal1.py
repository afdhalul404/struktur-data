# 1. input 3 angka tmapilkan nilai paling besar dan paling kecil
a = int(input("Masukan nial a: "))
b = int(input("Masukan nial b: "))
c = int(input("Masukan nial c: "))

if a > b and a > c:
    if b < c:
        print(f"nilai terbesar adalah : {a}")
        print(f"nilai terkecil adalah : {b}")
    else:
        print(f"nilai terbesar adalah : {a}")
        print(f"nilai terkecil adalah : {c}")
elif b > a and b > c:
    if c < b:
        print(f"nilai terbesar adalah : {b}")
        print(f"nilai terkecil adalah : {a}")
    else:
        print(f"nilai terkecil adalah : {b}")
        print(f"nilai terbesar adalah : {a}")

else:
    if c < b:
        print(f"nilai terbesar adalah : {c}")
        print(f"nilai terkecil adalah : {b}")
    else:
        print(f"nilai terbesar adalah : {c}")
        print(f"nilai terkecil adalah : {a}")
