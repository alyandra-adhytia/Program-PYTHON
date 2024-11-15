# dibuat oleh : alyandra adhytia sopyan
# tanggal dibuat : 15 november 2024
# program konversi suhu
print("Konversi Suhu: Celsius ke Fahrenheit atau sebaliknya")
print("1. Celsius ke Fahrenheit")
print("2. Fahrenheit ke Celsius")

pilihan = input("Masukkan pilihan (1/2): ")

if pilihan == '1':
    celsius = float(input("Masukkan suhu dalam Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit}°F")
elif pilihan == '2':
    fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F = {celsius}°C")
else:
    print("Pilihan tidak valid!")