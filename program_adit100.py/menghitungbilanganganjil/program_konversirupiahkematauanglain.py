# dibuat oleh : alyandra adhytia sopyan
# tanggal dibuat : 15 november 2024
# Program konversi Rupiah ke USD dan Euro
100
rupiah = float(input("Masukkan jumlah Rupiah: "))

kurs_usd = 15000  # Contoh nilai kurs
kurs_euro = 16000  # Contoh nilai kurs

usd = rupiah / kurs_usd
euro = rupiah / kurs_euro

print(f"{rupiah} Rupiah = {usd:.2f} USD")
print(f"{rupiah} Rupiah = {euro:.2f} Euro")