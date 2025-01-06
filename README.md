1. Class Data
Fungsi: Untuk merepresentasikan objek mahasiswa.
Attribute:
o	nama: Menyimpan nama mahasiswa.
o	nim: Menyimpan NIM (Nomor Induk Mahasiswa) mahasiswa.
Constructor (init): Diinisialisasi dengan atribut nama dan nim.

Contoh:
mahasiswa = Data("Nadia", "312410258")


2.	 Class View
Fungsi: Bertanggung jawab untuk menampilkan data mahasiswa dalam bentuk tabel.
Method:
o	tampilkan_data: Fungsi statis yang menerima daftar objek mahasiswa dan mencetak data mereka dalam format tabel.

Format tampilan:
NIM                Nama                
======================
312410258       Nadia


3.	 Class Process
Fungsi: Mengelola input data dari pengguna.
Method:
o	input_data: Fungsi untuk menerima input nama dan NIM mahasiswa dari pengguna, memvalidasi input, dan menyimpan objek mahasiswa ke dalam list (mahasiswa_list).
Validasi:
	NIM harus berupa angka.
	Nama tidak boleh kosong.

o	Program terus menerima input hingga pengguna mengetikkan "exit".

Proses:
	Meminta NIM: Jika NIM bukan angka, muncul pesan error.
	Meminta Nama: Jika nama kosong, muncul pesan error.
	Jika valid, data dimasukkan ke dalam list mahasiswa_list.


4.	 Fungsi main()
Fungsi:
o	Menjalankan seluruh program.
o	Memanggil Process.input_data untuk mengumpulkan data mahasiswa.
o	Memanggil View.tampilkan_data untuk menampilkan daftar mahasiswa yang telah dimasukkan.


5.	 Bagian if name == "main":
Fungsi: Memastikan program hanya dijalankan ketika file ini dijalankan secara langsung
Memanggil fungsi main() untuk menjalankan program.

 *Contoh Jalannya Program:

INPUT

![Screenshot 2025-01-06 094200](https://github.com/user-attachments/assets/e09b083b-2211-4c01-958b-d02ef89aa8db)












OUTPUT

![Screenshot 2025-01-06 094211](https://github.com/user-attachments/assets/afba33eb-480f-4bba-83bf-3513e19b0bb8)


