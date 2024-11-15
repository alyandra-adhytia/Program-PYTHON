# dibuat oleh : alyandra adhytia sopyan
# tanggal dibuat : 15 november 2024
# Program untuk menghitung harga setelah diskon

harga_awal = float(input("Masukkan harga awal: "))
diskon = float(input("Masukkan persentase diskon: "))

harga_akhir = harga_awal - (harga_awal * diskon / 100)
print(f"Harga setelah diskon adalah: {harga_akhir}")