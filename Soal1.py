#dictionary sumber
angka_dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

#menampilkan header
print("key value item")

#menggunakan enumerate untuk menunjukkan pendekatan lain (walau item tetap key)
for kunci in angka_dict:
    nilai = angka_dict[kunci]
    elemen = kunci  #item di sini dianggap sama dengan key, sesuai contoh
    print(f"{kunci}   {nilai}    {elemen}")
