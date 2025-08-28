#print()
print("Hallo dunia, nama ku Diky Rudianto")

#variabel
nama = "Diky Rudianto"
umur = 19
tinggi = 165.6
hobi = "belajar, belajar, belajar"
pelajar = True
print(nama)
print(umur)
print(tinggi)
print(hobi)
print(pelajar)

#tipe data
print(type(nama))
print(type(umur))
print(type(tinggi))
print(type(hobi))
print(type(pelajar))

#f-string
print(f"Nama saya {nama}, umur saya {umur + 2} tahun, hobi saya {hobi + " dan belajar"}, dan status saya sebagai pelajar merupakan {pelajar}")

#operasi dasar
x = 20
y = 7
print(x + y) 
print(x - y)
print(x * y)
print(x / y)
print(x ** y)

#list
angka = [1,2,3,4,5,6]
print(angka[2])
print(angka[4] + angka[2])
print(angka[5] + 100)

#loop
anggota = ["satu","dua","tiga",'empat','lima']
for i in anggota :
    print('Anggota', i)
for i in range(0, 100, 20):
    print('Angka', i)

#fungsi
def kali_tiga(angka):
    return angka * 3
def kali_dua(angka):
    return angka * 2
print(kali_tiga(2))
print(kali_dua(4))

#loop&fungsi
def cek_ganjil(angka):
    return angka % 2 == 1
print(cek_ganjil(10))
for i in angka:
    if cek_ganjil(i):
        print(f"{i} adalah ganjil")
    else:
        print(f"{i} adalah genap")

print(5 == 4)