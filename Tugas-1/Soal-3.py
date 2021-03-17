teori = float(input("Masukkan nilai ujian teori: "))
praktek = float(input("Masukkan nilai ujian praktek: "))
if teori >= 70 and praktek >= 70:
    print("Selamat, Anda lulus!")
elif teori < 70 and praktek >= 70:
    print("Anda harus mengulang ujian teori!")
elif teori >= 70 and praktek < 70:
    print("Anda harus mengulang ujian praktek!")
else:
    print("Anda harus mengulang ujian teori dan praktek!")