#list warna dan kode warna
warna_nama = ['red', 'green', 'blue']
warna_kode = ['#FF0000', '#008000', '#0000FF']

#dictionary kosong untuk menampung hasil
peta_warna = {}

#memasukkan pasangan key-value ke dalam dictionary secara manual
for i in range(len(warna_nama)):
    kunci = warna_nama[i]
    nilai = warna_kode[i]
    peta_warna[kunci] = nilai

#menampilkan hasil dictionary
print(peta_warna)
