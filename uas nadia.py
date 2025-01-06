class Data:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

class View:
    def tampilkan_data(mahasiswa_list):
        print(f"{'NIM':<10} {'Nama':<20}")
        print("=" * 30)
        for mhs in mahasiswa_list:
            print(f"{mhs.nim:<10} {mhs.nama:<20}")

class Process:
    def input_data():
        mahasiswa_list = []
        while True:
            try:
                nim = input("Masukan Nim (atau ketik 'exit' untuk keluar): ")
                if nim.lower() == 'exit':
                    break
                if not nim.isdigit():
                    raise ValueError("NIM harus berupa angka.")
                    
                nama = input("Masukkan Nama: ")
                if not nama:
                    raise ValueError("Nama tidak boleh kosong.")
                    
                mahasiswa = Data(nama, nim)
                mahasiswa_list.append(mahasiswa)
            except ValueError as e:
                print(f"Error: {e}")
        return mahasiswa_list

def main():
    mahasiswa_list = Process.input_data()
    View.tampilkan_data(mahasiswa_list)

if __name__ == "__main__":
    main()