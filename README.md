# KELASTAMBAH Remove Background
![KELASTAMBAH](https://github.com/KELASTAMBAH/KELASTAMBAH/blob/main/ktkt.png)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

KELASTAMBAH Remove Background adalah sebuah program Python yang digunakan untuk menghapus latar belakang gambar. Program ini menggunakan API Remove.bg untuk menghapus latar belakang gambar dengan cepat dan akurat.

## Fitur
- Dapat menghapus latar belakang gambar dengan cepat dan akurat
- Dapat mengatasi masalah transparansi dan edge yang tidak rata
- Mendukung berbagai format gambar, seperti PNG, JPG, dan BMP

## Persyaratan Instalasi
1. Pastikan Anda sudah menginstall Python 3 dan library `requests`
2. Daftar dan dapatkan API Key di [remove.bg](https://www.remove.bg/api) 


## Instalasi
```bash
# Clone repositori ini
git clone https://github.com/KELASTAMBAH/KT-Remove-Background.git
cd KT-Remove-Background

# Masukkan API key anda pada baris ke-5 di file kt.rb.py
vi kt.rb.py

# Buat folder output
mkdir output

# Jalankan program
python3 kt.rb.py
```

## Penggunaan
1. Masukkan path gambar yang ingin digunakan melalui input saat menjalankan program
2. Gambar hasil akan disimpan dalam folder `output/` dengan nama "kt.rb_[timestamp].png"

## Kontribusi
Kami sangat menyambut kontribusi dari komunitas. Jika Anda ingin berkontribusi, silakan fork repositori ini dan buat perubahan yang diinginkan. Setelah itu, buat permintaan pull untuk menyatukan perubahan Anda ke repositori utama.

## Lisensi
KELASTAMBAH Remove Background dilisensikan di bawah Lisensi MIT. Lihat file [LICENSE](LICENSE) untuk informasi lebih lanjut.
