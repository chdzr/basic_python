nilai_teori = float(input("Masukkan Nilai Teori : "))
nilai_praktek = float(input("Masukkan Nilai Praktek : "))

if nilai_teori >= 70 and nilai_praktek >= 70:
    print("Selamat, anda lulus!")
elif nilai_teori >= 70 and nilai_praktek < 70:
    print("Anda harus mengulang ujian praktek.")
elif nilai_teori < 70 and nilai_praktek >= 70:
    print("Anda harus mengulang ujian teori.")
else:
    print("Anda harus mengulang ujian teori dan praktek.")
