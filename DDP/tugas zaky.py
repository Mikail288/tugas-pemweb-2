#1.buatlah sebuah program python yang menghasilkan nilai perbandingan 2 variabel
a=10
b=56

print(a&b)
print(a|b)
print(a//b)
print(a^b)
print(a>>b)
print(a<<b)
print(a*b)

#2.buat program python menggunakan if,elif an else untuk konversi suhu
#celsius konverter
choice = 1
nilaiSuhu =  float(30)
if choice == 1:
    #Celsius ke Fahrenheit
    hasil =  (nilaiSuhu * 9/5) + 32
    print(nilaiSuhu,"Celsius sama dengan",hasil,"Fahrenheit")
    #Celsius ke kelvin
elif choice == 2:
    hasil = nilaiSuhu + 273.15
    print(nilaiSuhu,"Celsius sama dengan",hasil,"Kelvin")
else:
    print("Pilihan tidak valid. Silakan pilih nomor dari 1 atau 2.")

#3.buat program python yang menghasilkan status mahasiswa berdasarkan keaktifannya
#keaktifan mahasiswa
#karena tidak ada deskripsi tugas, saya buat dengan parameter kehadiran 0 - 100
mahasiswa = "zaky"
presensi = 80
if(presensi > 75 and presensi <= 100):
    status = "aktif"
else:
    status = "Tidak aktif"
print(mahasiswa,"termasuk mahasiswa yang",status)

#4.buat program kalkulator sederhana
#kalkulator simpel
#Variabel inputan user
angkaPertama = 4
angkaKedua = 78
pilihan = 4

if(pilihan == 1):
    print(angkaPertama,"Ditambah dengan",angkaKedua,"hasilnya:")
    hasil= angkaPertama + angkaKedua
elif(pilihan == 2):
    print(angkaPertama,"Dikurang dengan",angkaKedua,"hasilnya:")
    hasil= angkaPertama - angkaKedua
elif(pilihan == 3):
    print(angkaPertama,"Dibagi dengan",angkaKedua,"hasilnya:")
    hasil= angkaPertama / angkaKedua
elif(pilihan == 4):
    print(angkaPertama,"Dikali dengan",angkaKedua,"hasilnya:")
    hasil= angkaPertama * angkaKedua
else:
    print("pilihan operator tidak valid")
print(hasil)