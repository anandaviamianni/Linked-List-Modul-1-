class node :
    def __init__(self, val = None):
        self.val = val
        self.next = None

class TokoBuku():
    def __init__(self):
        self.head = None
    
    def add(self, data_in):
        NewNode = node(data_in)
        if self.head is None:
            self.head = NewNode
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = NewNode

    def deleteAtHead(self):
        temp = self.head
        self.head = self.head.next

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
            print (printval.val)
            printval = printval.next

tampil = TokoBuku()

def data():
    print ("\n\n *** Bookstore Distributor Data ***")
    print("1. Author")
    print("2. Editor")
    print("3. Publisher")
    print("0. Exit")
    work = int(input("Select Your Job : "))
    if work == 1:
        nama = input("Input Your Name Here : ")
        while True:
            print("Welcome To The App ", nama)
            print("a. Add Name Of a Bookstore")
            print("b. Delete Select Bookstore")
            print("c. Delete First Bookstore Data")
            print("d. Show Bookstore Data")
            print("e. Back To The First Menu")
            action = input("Select Action: ")
            if action == "a":
                BookStoreName = str(input("Add Name of the Bookstore Here\t: "))
                tampil.add(BookStoreName)
            elif action == "b":
                print("Bookstore Data : ");tampil.listprint()
                delete = input("Insert Bookstore That You Want To Delete: ")
                tampil.RemoveNode(delete)
                print("Bookstore Data Has Been Updated ");tampil.listprint()
            elif action =="c":
                tampil.deleteAtHead()
                print("Bookstore Data Has Been Updated ");tampil.listprint()
            elif action == "d":
                tampil.listprint()
            elif action == "e":
                return data()
    elif work == 2:
        nama = input("Input Your Name Here : ")
        while True:
            print("Welcome To The App ", nama)
            print("a. Add Name Of a Bookstore")
            print("b. Delete Select Bookstore")
            print("c. Delete First Bookstore Data")
            print("d. Show Bookstore Data")
            print("e. Back To The First Menu")
            action = input("Select Action: ")
            if action == "a":
                BookStoreName = str(input("Add Name of the Bookstore Here\t: "))
                tampil.add(BookStoreName)
            elif action == "b":
                print("Bookstore Data : ");tampil.listprint()
                delete = input("Insert Bookstore That You Want To Delete: ")
                tampil.RemoveNode(delete)
                print("Bookstore Data Has Been Updated ");tampil.listprint()
            elif action =="c":
                tampil.deleteAtHead()
                print("Bookstore Data Has Been Updated ");tampil.listprint()
            elif action == "d":
                tampil.listprint()
            elif action == "e":
                return data()
    elif work == 3:
        nama = input("Input Your Name Here : ")
        while True:
            print("Welcome To The App ", nama)
            print("a. Add Name Of a Bookstore")
            print("b. Delete Select Bookstore")
            print("c. Delete First Bookstore Data")
            print("d. Show Bookstore Data")
            print("e. Back To The First Menu")
            action = input("Select Action: ")
            if action == "a":
                BookStoreName = str(input("Add Name of the Bookstore Here\t: "))
                tampil.add(BookStoreName)
            elif action == "b":
                print("Bookstore Data : ");tampil.listprint()
                delete = input("Insert Bookstore That You Want To Delete: ")
                tampil.RemoveNode(delete)
                print("Bookstore Data Has Been Updated ");tampil.listprint()
            elif action =="c":
                tampil.deleteAtHead()
                print("Bookstore Data Has Been Updated ");tampil.listprint()
            elif action == "d":
                tampil.listprint()
            elif action == "e":
                return data()
    elif work == 0:
        print("Program Selesai")
        exit()
    else:
        print("Intruksi Salah")
data()