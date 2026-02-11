#Latihan 1
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

        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print(f"Elemen {key} tidak ditemukan.")
            return

        prev.next = temp.next
        temp = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")


# ===== Program Utama =====
ll = LinkedList()

data = input("Masukkan elemen Linked List (pisahkan dengan koma): ")
for x in data.split(","):
    ll.insert_at_end(int(x.strip()))

print("\nLinked List awal:")
ll.display()

hapus = int(input("Masukkan angka yang ingin dihapus: "))
ll.delete_node(hapus)

print("\nLinked List setelah penghapusan:")
ll.display()

#Latihan 2
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
        while True:
            if temp.data == key:
                print(f"Elemen {key} ditemukan dalam Circular Linked List.")
                return
            temp = temp.next
            if temp == self.head:
                break

        print(f"Elemen {key} tidak ditemukan dalam Circular Linked List.")


# ===== Program Utama =====
cll = CircularSinglyLinkedList()

data = input("Masukkan elemen Circular Linked List (pisahkan dengan koma): ").strip()

if data:
    for x in data.split(","):
        cll.insert_at_end(int(x.strip()))
else:
    print("List kosong.")

cari = int(input("Masukkan elemen yang ingin dicari: "))
cll.search(cari)

#Latihan 4
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

    def merge(self, other):
        if not self.head:
            self.head = other.head
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = other.head

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")


# ===== Program Utama =====
ll1 = LinkedList()
ll2 = LinkedList()

data1 = input("Masukkan elemen Linked List 1 (pisahkan dengan koma): ").strip()
if data1:
    for x in data1.split(","):
        ll1.insert_at_end(int(x.strip()))

data2 = input("Masukkan elemen Linked List 2 (pisahkan dengan koma): ").strip()
if data2:
    for x in data2.split(","):
        ll2.insert_at_end(int(x.strip()))

print("\nLinked List 1:")
ll1.display()

print("Linked List 2:")
if ll2.head:
    ll2.display()
else:
    print("kosong")

ll1.merge(ll2)

print("\nLinked List setelah digabungkan:")
ll1.display()