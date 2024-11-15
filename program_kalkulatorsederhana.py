# dibuat oleh : alyndra adhytia sopyan
# tanggal dibuat : 15 november 2024
# program kalkulator sederhana

print("Kalkulator Sederhana")
print("Pilih operasi:")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")

# Meminta input dari pengguna
pilihan = input("Masukkan pilihan (1/2/3/4): ")
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

if pilihan == '1':
    print("Hasil:", angka1 + angka2)
elif pilihan == '2':
    print("Hasil:", angka1 - angka2)
elif pilihan == '3':
    print("Hasil:", angka1 * angka2)
elif pilihan == '4':
    if angka2 != 0:
        print("Hasil:", angka1 / angka2)
    else:
        print("Tidak dapat membagi dengan nol!")
else:
    print("Pilihan tidak valid!")