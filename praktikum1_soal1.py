# soal no 1
print('1. Fahrenheit --> Reamur')
print('2. Reamur --> Fahrenheit')

pilih = int(input('Masukan pilihan :'))

if (pilih == 1):
    fahrenhait = float(input('Masukan suhu Fahrenhait : '))
    reamur = ((4/9)*fahrenhait-32)
    print('Nilai Fahrenhait = ', fahrenhait)
    print('Fahrenhait --> Reamur = ', reamur, 'F')
else:
    reamur = float(input('Masukan suhu reamur : '))
    fahrenhait = ((9/4)+reamur+32)
    print('Nilai Reamur = ', reamur)
    print('Reamur --> Fahrenhait = ', fahrenhait, 'R')
