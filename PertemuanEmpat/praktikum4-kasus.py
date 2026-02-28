####################################################################
# Nama file: praktikum4-kasus.py
# Nama: Nayla Aqila Argia
# NIM: J0403251142
# Kelas: B2
####################################################################


# Sistem Antrian Akademik menggunakan Queue (FIFO)
# Implementasi Queue TIDAK menggunakan list,
# tetapi menggunakan Linked List (Node + pointer).


# Node adalah unit terkecil dari Linked List.
# Setiap node menyimpan:
# - data mahasiswa (NIM dan Nama)
# - pointer next untuk menunjuk ke node berikutnya
class Node:
    def __init__(self, nim, nama):
        self.nim = nim          # menyimpan NIM mahasiswa
        self.nama = nama        # menyimpan nama mahasiswa
        self.next = None        # pointer ke node berikutnya
                               # awalnya None karena belum terhubung


# ===============================================================
# 2) Class Queue Akademik
# Queue menerapkan prinsip FIFO (First In First Out)
# - front : menunjuk mahasiswa paling depan (yang dilayani dulu)
# - rear  : menunjuk mahasiswa paling belakang (tempat masuk data)
# ===============================================================
class queueAkademik:
    def __init__(self):
        # Saat queue dibuat, masih kosong
        self.front = None      # belum ada mahasiswa di depan
        self.rear = None       # belum ada mahasiswa di belakang

    def is_empty(self):
        # Queue dikatakan kosong jika front = None
        return self.front is None


    # ===========================================================
    # Enqueue
    # Fungsi untuk MENAMBAH mahasiswa ke BELAKANG antrian
    # ===========================================================
    def enqueue(self, nim, nama):
        # Membuat node baru untuk mahasiswa yang masuk antrian
        nodeBaru = Node(nim, nama)

        # Jika antrian masih kosong
        if self.is_empty():
            # front dan rear sama-sama menunjuk ke node baru
            self.front = nodeBaru
            self.rear = nodeBaru
        else:
            # Jika antrian sudah ada isinya:
            # 1. rear lama menunjuk ke node baru
            self.rear.next = nodeBaru

            # 2. rear dipindahkan ke node baru
            self.rear = nodeBaru


    # ===========================================================
    # Dequeue
    # Fungsi untuk MELAYANI (menghapus) mahasiswa dari DEPAN antrian
    # ===========================================================
    def dequeue(self):
        # Jika antrian kosong, tidak bisa melayani siapa pun
        if self.is_empty():
            print("Antrian kosong, tidak ada data yang bisa dilayani.")
            return None

        # Simpan data mahasiswa yang akan dilayani
        node_dilayani = self.front

        # Geser front ke node berikutnya
        # Artinya mahasiswa paling depan sudah keluar dari antrian
        self.front = self.front.next

        # Jika setelah digeser front menjadi None,
        # berarti antrian sekarang kosong
        if self.front is None:
            self.rear = None

        # Kembalikan mahasiswa yang dilayani
        return node_dilayani


    # ===========================================================
    # Menampilkan seluruh isi antrian
    # ===========================================================
    def tampilkan(self):
        # Jika antrian kosong, langsung tampilkan pesan
        if self.is_empty():
            print("Antrian kosong.")
            return

        print("Daftar Antrian Mahasiswa (Front -> Rear):")

        current = self.front   # mulai dari mahasiswa paling depan
        no = 1                 # nomor urut tampilan

        # Loop berjalan selama current belum None
        while current:
            print(f"{no}. NIM: {current.nim}, Nama: {current.nama}")
            current = current.next   # pindah ke node berikutnya
            no += 1

# 3) Program Utama (Menu Interaktif)
def main():
    # Membuat objek queue akademik
    q = queueAkademik()

    # Perulangan agar menu terus muncul sampai user memilih keluar
    while True:
        print("\n==== Sistem Antrian Akademik ====")
        print("1. Tambah Mahasiswa")
        print("2. Layani Mahasiswa")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilihan = input("Masukkan pilihan (1-4): ").strip()

        # Menu 1: Tambah Mahasiswa
        if pilihan == "1":
            nim = input("Masukkan NIM mahasiswa: ").strip()
            nama = input("Masukkan nama mahasiswa: ").strip()

            # Data dimasukkan ke antrian menggunakan enqueue
            q.enqueue(nim, nama)
            print("Mahasiswa berhasil ditambahkan ke antrian.")

        # Menu 2: Layani Mahasiswa
        elif pilihan == "2":
            dilayani = q.dequeue()

            # Jika dequeue berhasil (tidak None)
            if dilayani:
                print(f"Mahasiswa Dilayani: {dilayani.nim} - {dilayani.nama}")

        # Menu 3: Lihat Antrian
        elif pilihan == "3":
            q.tampilkan()

        # Menu 4: Keluar Program
        elif pilihan == "4":
            print("Program selesai. Terima kasih.")
            break

        
        # Jika input menu tidak valid
        else:
            print("Pilihan tidak valid.")



# Penanda bahwa file ini dijalankan langsung
if __name__ == "__main__":
    main()



# CATATAN PR:
# - Program ini menggunakan Queue berbasis Linked List
# - Tidak menggunakan list Python sama sekali
# - Prinsip FIFO diterapkan dengan benar
# - Untuk tugas hands-on, kasus diganti menjadi bengkel motor