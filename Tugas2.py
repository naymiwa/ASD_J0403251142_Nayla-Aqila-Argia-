#Latihan 1: Implementasi fungsi untuk menghapus node dgn nilai tertentu
print("Latihan 1")
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_node(self, key):
        temp = self.head

        # Jika node pertama yang dihapus
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next
        temp = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")


# Contoh penggunaan
ll = LinkedList()
ll.insert_at_end(13)
ll.insert_at_end(5)
ll.insert_at_end(13)
ll.insert_at_end(2)

print("Sebelum dihapus:")
ll.display()

ll.delete_node(13)

print("Setelah 13 dihapus:")
ll.display()

#Latihan 2: Buat	kode	Implementasikan	Pencarian	pada	node	tertentu	Single	
print("Latihan 2")
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def search(self, key):
        if not self.head:
            print("Circular Linked List kosong. Tidak ada elemen yang bisa dicari.")
            return

        temp = self.head
        if temp.data == key:
            print(f"Elemen {key} ditemukan dalam Circular Linked List.")
            return

        temp = temp.next
        while temp != self.head:
            if temp.data == key:
                print(f"Elemen {key} ditemukan dalam Circular Linked List.")
                return
            temp = temp.next

        print(f"Elemen {key} tidak ditemukan dalam Circular Linked List.")


# Contoh penggunaan
cll = CircularSinglyLinkedList()
cll.insert_at_end(3)
cll.insert_at_end(7)
cll.insert_at_end(12)
cll.insert_at_end(19)
cll.insert_at_end(25)

cll.search(12)

#Latihan 4: Buat	metode	untuk	menggabungkan	dua	single	linked	list	menjadi	satu linked	list baru
print("Latihan 4")
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    def merge(self, other_list):
        if not self.head:
            self.head = other_list.head
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = other_list.head


# Contoh penggunaan
ll1 = LinkedList()
ll2 = LinkedList()

for i in [1, 3, 5, 7]:
    ll1.insert_at_end(i)

for i in [2, 4, 6, 8]:
    ll2.insert_at_end(i)

print("Linked List 1:")
ll1.display()

print("Linked List 2:")
ll2.display()

ll1.merge(ll2)

print("Linked List setelah digabungkan:")
ll1.display()