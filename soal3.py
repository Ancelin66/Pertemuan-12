#meminta input nama file dari user
file_nama = input("Masukkan nama file: ")

try:
    #buka file
    arsip = open(file_nama, 'r')

    #buat dictionary kosong untuk menghitung
    frekuensi_email = dict()

    #proses setiap baris dalam file
    for isi in arsip:
        #hanya baris yang dimulai dengan 'From '
        if isi.startswith('From '):
            potong = isi.strip().split()
            alamat = potong[1]

            #cek apakah alamat sudah ada di dict
            if alamat in frekuensi_email:
                frekuensi_email[alamat] += 1
            else:
                frekuensi_email[alamat] = 1

    #cetak hasil akhir
    for pengirim, jumlah in frekuensi_email.items():
        print(f"{pengirim}: {jumlah}")

except FileNotFoundError:
    print("Oops! File tidak ditemukan.")
