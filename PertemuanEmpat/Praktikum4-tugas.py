####################################################################
# Nama file: Praktikum4-tugas.py
# Nama     : Nayla Aqila Argia
# NIM      : J0403251142
# Kelas    : B2
####################################################################

# Studi Kasus:
# Sistem Antrian Bengkel Motor
# Struktur Data: Queue (FIFO) berbasis Linked List
# Data pelanggan: nomor antrian, nama pelanggan, jenis servis

# ================================================================
# 1) Definisi Node (Unit dasar Linked List)
# ================================================================
class Node:
    def __init__(self, no_antrian, nama, servis):
        self.no_antrian = no_antrian   # nomor antrian pelanggan
        self.nama = nama               # nama pelanggan
        self.servis = servis           # jenis servis
        self.next = None               # pointer ke node berikutnya


# ================================================================
# 2) Definisi Queue Bengkel
# ================================================================
class QueueBengkel:
    def __init__(self):
        self.front = None   # menunjuk pelanggan terdepan
        self.rear = None    # menunjuk pelanggan terakhir

    def is_empty(self):
        # Queue kosong jika front bernilai None
        return self.front is None

    # ------------------------------------------------------------
    # Enqueue: menambahkan pelanggan ke belakang antrian
    # ------------------------------------------------------------
    def enqueue(self, no_antrian, nama, servis):
        node_baru = Node(no_antrian, nama, servis)

        # Jika antrian kosong
        if self.is_empty():
            self.front = node_baru
            self.rear = node_baru
        else:
            # Hubungkan node terakhir ke node baru
            self.rear.next = node_baru
            self.rear = node_baru

        print("Pelanggan berhasil ditambahkan ke antrian.")

    # ------------------------------------------------------------
    # Dequeue: melayani pelanggan terdepan
    # ------------------------------------------------------------
    def dequeue(self):
        if self.is_empty():
            print("Antrian kosong, tidak ada pelanggan yang bisa dilayani.")
            return None

        # Simpan pelanggan yang akan dilayani
        pelanggan_dilayani = self.front

        # Geser front ke node berikutnya
        self.front = self.front.next

        # Jika setelah dequeue antrian menjadi kosong
        if self.front is None:
            self.rear = None

        return pelanggan_dilayani

    # ------------------------------------------------------------
    # Menampilkan seluruh isi antrian
    # ------------------------------------------------------------
    def tampilkan(self):
        if self.is_empty():
            print("Antrian bengkel kosong.")
            return

        print("\nDaftar Antrian Bengkel (Front -> Rear):")
        current = self.front
        no = 1

        # Traversal dari front hingga None
        while current is not None:
            print(f"{no}. No Antrian: {current.no_antrian}, "
                  f"Nama: {current.nama}, Servis: {current.servis}")
            current = current.next
            no += 1


# ================================================================
# 3) Program Utama (Menu Interaktif)
# ================================================================
def main():
    q = QueueBengkel()

    while True:
        print("\n=== Sistem Antrian Bengkel ===")
        print("1. Tambah Pelanggan")
        print("2. Layani Pelanggan")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilihan = input("Masukkan pilihan (1-4): ").strip()

        if pilihan == "1":
            no_antrian = input("Masukkan No Antrian  : ").strip()
            nama = input("Masukkan Nama Pelanggan: ").strip()
            servis = input("Masukkan Jenis Servis : ").strip()

            # Validasi input sederhana
            if no_antrian == "" or nama == "" or servis == "":
                print("Data tidak boleh kosong.")
                continue

            q.enqueue(no_antrian, nama, servis)

        elif pilihan == "2":
            pelanggan = q.dequeue()
            if pelanggan:
                print(f"Pelanggan Dilayani -> "
                      f"No Antrian: {pelanggan.no_antrian}, "
                      f"Nama: {pelanggan.nama}, "
                      f"Servis: {pelanggan.servis}")

        elif pilihan == "3":
            q.tampilkan()

        elif pilihan == "4":
            print("Program selesai. Terima kasih.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih 1-4.")


# ================================================================
# 4) Penanda eksekusi program utama
# ================================================================
if __name__ == "__main__":
    main()