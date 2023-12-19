import math

def tambah(angka1, angka2):
    return angka1 + angka2

def kurang(angka1, angka2):
    return angka1 - angka2

def kali(angka1, angka2):
    return angka1 * angka2

def bagi(angka1, angka2):
    if angka2 == 0:
        return "Tidak dapat membagi dengan nol"
    return angka1 / angka2

while True:
    print("Pilih operasi:")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("5. Perpangkatan")
    print("6. Logaritma")
    print("7. Akar Pangkat 2")
    print("8. Akar Pangkat 3")
    print("9. Keluar")

    pilihan = input("Masukkan pilihan (1-9): ")

    if pilihan == "9":
        print("Keluar dari kalkulator.")
        break

    if pilihan not in ("1", "2", "3", "4", "5", "6", "7", "8"):
        print("Pilihan tidak valid. Silakan coba lagi.")
        continue

    try:
        angka1 = float(input("Masukkan angka pertama: ")) if pilihan != "5" and pilihan != "6" and pilihan != "7" and pilihan != "8" else float(input("Masukkan angka: "))
        angka2 = float(input("Masukkan angka kedua: ")) if pilihan != "5" and pilihan != "6" and pilihan != "7" and pilihan != "8" else None
    except ValueError:
        print("Masukkan angka yang valid.")
        continue

    if pilihan == "1":
        print("Hasil penambahan:", tambah(angka1, angka2))
    elif pilihan == "2":
        print("Hasil pengurangan:", kurang(angka1, angka2))
    elif pilihan == "3":
        print("Hasil perkalian:", kali(angka1, angka2))
    elif pilihan == "4":
        print("Hasil pembagian:", bagi(angka1, angka2))
    elif pilihan == "5":
        angka2 = float(input("Masukkan eksponen: "))
        print("Hasil perpangkatan:", math.pow(angka1, angka2))
    elif pilihan == "6":
        basis = float(input("Masukkan basis: "))
        print("Hasil logaritma:", math.log(angka1, basis))
    elif pilihan == "7":
        if angka1 < 0:
            print("Akar pangkat 2 tidak valid untuk bilangan negatif.")
        else:
            print("Akar pangkat 2:", math.sqrt(angka1))
    elif pilihan == "8":
        if angka1 < 0:
            print("Akar pangkat 3 tidak valid untuk bilangan negatif.")
        else:
            print("Akar pangkat 3:", angka1 ** (1 / 3))

    lanjutkan = input("Lanjutkan? (y/n): ")
    if lanjutkan.lower() != 'y':
        print("Keluar dari kalkulator.")
        break
