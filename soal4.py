# Meminta nama file dari user
berkas = input("Masukkan nama file: ")

try:
    # Buka file
    sumber = open(berkas, 'r')

    # Dictionary untuk menyimpan jumlah domain
    statistik_domain = {}

    # Membaca baris satu per satu
    for teks in sumber:
        if teks.startswith("From "):
            kata = teks.split()
            pengirim = kata[1]
            pecah = pengirim.split('@')
            nama_domain = pecah[1]

            # Tambahkan atau update jumlah domain
            if nama_domain in statistik_domain:
                statistik_domain[nama_domain] += 1
            else:
                statistik_domain[nama_domain] = 1

    # Menampilkan hasil
    print(statistik_domain)

except FileNotFoundError:
    print("Berkas tidak ditemukan. Silakan cek nama file dan coba lagi.")
