class node :
    def __init__(self, val = None):
        self.val = val
        self.next = None

class TokoBuku():
    def __init__(self):
        self.head = None
    
    def add(self, data_in):
        NewMode = node(data_in)
        NewMode.next = self.head
        self.head = NewMode

    def RemoveNode(self, RemoveKey):
        HeadVal = self.head

        if HeadVal is not None:
            if HeadVal.val == RemoveKey:
                self.head = HeadVal.next
                HeadVal = None
                return
        
        while HeadVal is not None:
            if HeadVal.val == RemoveKey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next

        if HeadVal is None:
            return
        prev.next = HeadVal.next
        HeadVal = None

    def listprint(self):
        printval = self.head
        while printval is not None:
            print(printval.val)
            printval = printval.next

list = TokoBuku()
list.head = node("Mon")
e2 = node("Tue")
e3 = node("Wed")
e4 = node("Thu")
list.head.next = e2
e2.next = e3
e3.next = e4
list.listprint()

edit = input("mau edit data? y/n : ")
if edit == "y":
    apa = input("Tambah / hapus? t/h : ")
    if apa == "t" :
        mana = input("Mau tambah data di mana? f/m/e : ")
        if mana == "f":
            data = input("Masukkan data : ")
            list.add(data)
            list.listprint()
else:
    print("Selesai")



