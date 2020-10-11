class Node: 
    def __init__(self, val = None): 
        self.val = val 
        self.next = None
  
class TokoBuku: 
    def __init__(self): 
        self.head = None

    def Add(self, new_value): 
        NewNode = Node(new_value) 
        if self.head is None: 
            self.head = NewNode 
            return
        current = self.head 
        while current.next is not None: 
            current = current.next
        current.next = NewNode

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

    def sortedMerge(self, a, b): 
        result = None
        if a == None: 
            return b 
        if b == None: 
            return a 
        if a.val <= b.val: 
            result = a 
            result.next = self.sortedMerge(a.next, b) 
        else: 
            result = b 
            result.next = self.sortedMerge(a, b.next) 
        return result 
      
    def mergeSort(self, h): 
        if h == None or h.next == None: 
            return h 
        middle = self.getMiddle(h) 
        nexttomiddle = middle.next
        middle.next = None
        left = self.mergeSort(h) 
        right = self.mergeSort(nexttomiddle) 
        sortedlist = self.sortedMerge(left, right) 
        return sortedlist 

    def getMiddle(self, head): 
        if (head == None): 
            return head 
        slow = head 
        fast = head 
        while (fast.next != None and 
               fast.next.next != None): 
            slow = slow.next
            fast = fast.next.next
        return slow 
 
def listprint(head): 
    if head is None: 
        print(' ') 
        return
    current = head
    count = 1
    while current: 
        print(str(count)+str("."), current.val,) 
        current = current.next
        count += 1
    print(' ') 
    
tampil = TokoBuku()
def menu():
    print ("\tProgram Penyimpan Ide Nama Tokoh")
    print ("1. Tambahkan Nama Tokoh")
    print ("2. Tampilkan Daftar Nama Tokoh")
    print ("0. Keluar")
    select = int(input("Masukkan Pilihan : "))
    if select == 1: 
        while True:
            inputs = str(input("Masukkan Nama Tokoh : "))
            tampil.Add(inputs)
            if inputs == "the end":
                tampil.RemoveNode("the end")
                break
            tampil.head = tampil.mergeSort(tampil.head)
        return menu()
    elif select == 2:
        print ("\tDaftar Nama Tokoh") 
        listprint(tampil.head) 
        return menu()
    elif select == 0:
        exit()
menu()
