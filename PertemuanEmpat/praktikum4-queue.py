# Nama  : Nayla Aqila Argia
# NIM   : J0403251142
# Kelas : B2

# ==================================================
# Implementasi Dasar : Queue berbasis Linked List
# ==================================================

# Class Node untuk menyimpan data dan pointer ke node berikutnya
class Node:
    def __init__(self, data):
        self.data = data      # menyimpan nilai/data
        self.next = None      # pointer ke node berikutnya (awal None)


# Class Queue dengan dua pointer : front dan rear
class QueueLL:
    def __init__(self):
        self.front = None     # pointer menunjuk elemen paling depan
        self.rear = None      # pointer menunjuk elemen paling belakang

    # Mengecek apakah queue kosong
    def is_empty(self):
        return self.front is None

    # Menambahkan data ke belakang queue (enqueue)
    def enqueue(self, data):
        nodeBaru = Node(data)     # membuat node baru

        # Jika queue masih kosong
        if self.is_empty():
            self.front = nodeBaru    # front menunjuk node baru
            self.rear = nodeBaru     # rear menunjuk node baru
        else:
            # Jika queue tidak kosong
            self.rear.next = nodeBaru  # hubungkan rear lama ke node baru
            self.rear = nodeBaru       # rear pindah ke node baru
            
    def dequeue(self):
    #Menghapus data dari depan 
        #1) lihat data paling depan
        data_terhapus = self.front.data 
    
        #2) geser front ke node berikutnya
        self.front = self.front.next
        
        #3) jika setelah digeser front menjadi none, berarti queue kosong, maka rear juga harus jadi none
        if self.front is None:
            self.rear = None
            
        return data_terhapus
            
    

    # Menampilkan isi queue dari front ke rear
    def tampilkan(self):
        if self.is_empty():
            print("Queue kosong")
            return

        current = self.front
        print("Front -> ", end="")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None (Rear)")

    
    

# ==================================================
# Program Utama
# ==================================================

# Instansiasi objek queue
q = QueueLL()

# Menambahkan elemen ke queue
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")

# Menampilkan isi queue
q.tampilkan()


q.dequeue()
q.tampilkan()
