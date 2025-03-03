# link-finder

**link-finder** adalah sebuah alat yang digunakan untuk mencari tautan "Dana kaget" dari situs Threads berdasarkan kata kunci yang ditentukan. Script ini memanfaatkan `requests` untuk mengambil data dari halaman Threads, kemudian mencari dan menampilkan tautan yang ditemukan.

## Fitur

- Mencari tautan dana kaget dari Threads.
- Menggunakan sesi dengan cookies dan header yang diatur untuk memastikan pengambilan data yang berhasil.
- Menyimpan hasil tautan yang ditemukan ke dalam file teks.

## Persyaratan

- Python 3.x
- Modul Python:
  - `requests`

Instalasi modul:
- `pip install requests`

## Cara menggunakan
- Clone repositories
  - `git clone https://github.com/Fajarrrrkylink-finder.git`
  - `cd dana-link-finder`
  - `python Run.py`
 
- Masukkan kata kunci yang ingin dicari pada Threads. Kata kunci dapat dipisah dengan koma jika ingin mencari beberapa sekaligus.
- Tautan yang ditemukan akan disimpan di file `Data/Done.txt` dan juga ditampilkan di terminal.
