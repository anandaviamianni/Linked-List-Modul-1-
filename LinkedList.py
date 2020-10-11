class Jadwal:
    class node :
        def __init__(self, element, next_node = None ):
            self.element = element
            self.next_node = next_node
    
    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        hasil = ""
        pointer = self.head
        while pointer != None:
            hasil = hasil + str(pointer.element) + ", "
            pointer = pointer.next_node
        return hasil
    
    def add(self, element):
        new_node = self.node(element)
        if(self.head == None):
            self.head = new_node
        else:
            pointer = self.head
            while pointer.next_node != None:
                pointer = pointer.next_node
            pointer.next_node = new_node
        self.size += 1

    def remove(self, key):  
        pointer = self.head  
        if (pointer is not None):  
            if (pointer.element == key):  
                self.head = pointer.next_node
                pointer = None
                return
        while(pointer is not None):  
            if pointer.element == key:  
                break
            prev = pointer  
            pointer = pointer.next_node
   
        if(pointer == None):  
            return

        prev.next_node = pointer.next_node
        self.size -= 1
        pointer = None

kegiatan = Jadwal()

def coba():
    print("\n\t=== Jadwal Hari Ini ===")
    print("1. Tambah Kegiatan")
    print("2. Hapus Kegiatan")
    print("0. Keluar")
    print("------------------")
    menu = input("Pilih menu? ")

    if menu == "1":
        td = str(input("Masukkan Kegiatan Hari Ini \t: "))
        kegiatan.add(td)
        print("Jadwal Hari Ini \t\t: ", str(kegiatan))
    elif menu == "2":
        print("Jadwal Hari Ini \t\t: ", str(kegiatan))
        hps = str(input("Kegiatan Yang Sudah Dilakukan \t:  "))
        kegiatan.remove(hps)
        print("Jadwal Sekarang \t\t: ", str(kegiatan))
    elif menu == "0":
        exit()
    else:
        print("Menu salah!") 
if __name__ == "__main__":
  while(True):
    coba()