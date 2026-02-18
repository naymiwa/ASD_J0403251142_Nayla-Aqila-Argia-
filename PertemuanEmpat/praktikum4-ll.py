
#Nama: Nayla Aqila Argia 
#NIM: J0403251142 
#Kelas: B2 

#==== Implementasi Dasar: Node dan Linked list ====

class Node:
    def __init__(self, data): #constructor = fungsi yg otomatis dijalankan saat objek dibuat
        self.data = data #objek yg digunakan untuk menyimpan nilai/data
        self.next = None #objek yg digunakan untuk menyimpan referensi ke node berikutnya (awal= none)
        
# 1) proses pertama pembuatan node     
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

# 2) hubungkan Node : A -> B -> C -> None
nodeA.next = nodeB
nodeB.next = nodeC
#nodeC.next = None

# 3) menentukan node pertama (head)
head = nodeA

# 4) Tranversal : dari head sampai none
current = head
while current is not  None:
    print(current.data)
    current = current.next
    
#   5) implementasi dasar linked list

class LinkedList:
    def __init__(self):
        self.head = None #awalnya kosong
        
    
    def insert_awal(self,data):
        #1 buat node baru
        nodeBaru = Node(data) #panggil class node
        
        #2 node baru menunjuk ke head lama
        nodeBaru.next = self.head #hubungkan node baru dengan head
        
        #3 head pindah ke node baru
        self.head = nodeBaru
        
    def hapus_awal(self):
        data_terhapus = self.head.data #peek dalam stack, melihat data yg dihapus
        #menghapus = menggeser head ke node berikutnya
        self.head = self.head.next 
        print("Node yang dihapus adalah: ", data_terhapus)
        
    def tampilkan(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

ll = LinkedList() #instantiasi objek ke class linked list
ll.insert_awal("X")
ll.insert_awal("Y")
ll.insert_awal("Z")
ll.tampilkan() #konsep stack, numpuk data (LIFO)
ll.hapus_awal()
ll.tampilkan()