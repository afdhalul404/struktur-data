pertemuan = int(input("jumlah pertemuan: "))
kehadiran = int(input("jumlah kehadiran: "))
pk = (kehadiran/pertemuan)*100

if pk >= 80:
    print("dapat megikuti ujian")
    print(f"presentasi kehadiran = {pk}%")
elif pk < 75:
    print(f"presentasi kehadiran = {pk}%")
    print("tidak dapat megikuti ujian")
