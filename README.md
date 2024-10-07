# Proyek Membangun Dashboard Bike Sharing System Data Analysis
Proyek ini merupakan bagian dari submission course Dicoding kelas Belajar Analisis Data dengan Python, projek ini adalah tugas menganalisis data dari dataset Bike Sharing Sistem yang kemudian divisualisasikan secara sederhana menggunakan Streamlit

# Gambaran Projek
Dalam Projek ini kami melalukan analisis data untuk melihat dan mengetahui Trend dari penyewaan sepede dilihat dari akumulasi dalam setahun, Bulan, Hari dalam Seminggu, Perjam dalam Sehari, Musim dan Kondisi Cuaca dari tahun 2011 dan 2012.

# Dataset yang Digunakan
Dalam proyek ini, saya menggunakan Bike Sharing Dataset yang mencakup data penggunaan sepeda harian dan per jam di sebuah kota. Beberapa variabel utama dalam dataset ini meliputi:
dteday: Tanggal
season: Musim
weathersit: Kondisi cuaca
temp: Suhu
cnt: Total penggunaan sepeda (gabungan pengguna kasual dan terdaftar)
#  Sumber Data:
Data yang digunakan di projek ini berasal dari Capital Bikeshare, semua dataset publik yang memuat data penyewaan sepeda di Washington D.C. Tahun 2011 dan Tahun 2012.

# Cara Menjalankan Proyek
Untuk menjalankan proyek ini, silakan ikuti langkah-langkah berikut:
1. Persiapan Environment
Pastikan Anda memiliki Python terinstal di sistem Anda.
2. Buat virtual environment baru (opsional, tetapi direkomendasikan): 
    ```bash
    python -m venv env
3. Aktifkan virtual environment:
    - Windows:
    ```bash
    .\env\Scripts\activate
  - MacOS/Linux:
    ```bash
    source env/bin/activate

4. Install semua library yang diperlukan dengan menjalankan perintah:
   ```bash
   pip install -r requirements.txt
5. Menjalankan Notebook
 - Buka Jupyter Notebook atau Google Colab.
 - Buka file notebook.ipynb di Jupyter atau Colab.
 - Jalankan semua sel untuk melihat hasil analisis dan visualisasi data.
6. Menjalankan Dashboard
 - Pastikan semua dependensi sudah terinstal.
 - Jalankan aplikasi Streamlit dengan perintah berikut di terminal:
    ```bash
    streamlit run dasboard/dasboard.py
Setelah perintah dijalankan, dashboard akan terbuka secara otomatis di browser Anda.

# Struktur Projek 
submission
 ```bash
 ├───dashboard
| ├───main_data.csv
| └───dashboard.py
├───data
| ├───day.csv
| └───hour.csv
├───notebook.ipynb
├───README.md
└───requirements.txt
└───url.txt
