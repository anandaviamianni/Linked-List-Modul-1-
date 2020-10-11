class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class JadwalKegiatan:
    def __init__(self):
        self.head = None

    def AddFirst(self, val):
        NewNode = Node(val)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = NewNode
        self.head = NewNode


    def AddLast(self, val):
        NewNode = Node(val)
        NewNode.next = None
        if self.head is None:
            NewNode.prev = None
            self.head = NewNode
            return
        last = self.head
        while (last.next is not None):
            last = last.next
        last.next = NewNode
        NewNode.prev = last
        return

    def AddByKey(self, AddKey, newdata):
        NewNode = Node(newdata)
        HeadVal = self.head

        while HeadVal is not None:
            if HeadVal.data == AddKey:
                NewNode.next = HeadVal.next
                HeadVal.next = NewNode
                break
            prev = HeadVal
            HeadVal = HeadVal.next
            
    def DeleteFirst(self):
        temp = self.head
        self.head = self.head.next

    def DeleteLast(self):
        temp = self.head
        while(temp.next is not None):
            prev  = temp
            temp = temp.next
        prev.next = None

    def DeleteByKey(self, RemoveKey):
        HeadVal = self.head

        if HeadVal is not None:
            if HeadVal.data == RemoveKey:
                self.head = HeadVal.next
                HeadVal = None
                return
        
        while HeadVal is not None:
            if HeadVal.data == RemoveKey:
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
        if a.data <= b.data: 
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
            
    def display(self, data):
        current = data
        count = 1
        while current is not None:
            print(str(count)+ str("."), current.data)
            current = current.next
            count += 1
            if current == None:
                break

tampil = JadwalKegiatan()

def data():
    nama = input("Input Your Name Here : ")
    while True:
        print("Welcome To The App ", nama)
        print("a. Add First Schedule")
        print("b. Add Last Schedule")
        print("c. Add Schedule By Key ")
        print("d. Delete First Schedule")
        print("e. Delete Last Schedule")
        print("f. Delete Schedule By Key")
        print("g. Sort Schedule")
        print("h. Show Entire Schedule")
        print("j. exit")
        action = input("Select Action: ")
        if action == "a":
            First = input("Input Your Work \t: ")
            day = input("Input Your Activities Day (DD/MM/YY) \t: ")
            hour = input("Input Your Activities Time (HH.MM)(24 Hour Format) \t: ")
            data = str(day)+str(" | ") + str(hour) + str(" | ") + str(First)
            tampil.AddFirst(data)
                
        elif action == "b":
            Last = input("Input Your Work: ")
            day = input("Input Your Activities Day (DD/MM/YY) \t: ")
            hour = input("Input Your Activities Time (HH.MM)(24 Hour Format) \t: ")
            data = str(day)+str(" | ") + str(hour) + str(" | ") + str(Last)
            tampil.AddLast(data)

        elif action =="c":
            print("Your Schedule has been updated:  ");tampil.display(tampil.head)
            #memasukan schedule sebelumnya, misalnya schedule sebelumnya adalah minum. [in between]
            print("\nFormat Input Previous Schedule (DD/MM/YY | HH.MM | <Previous Schedule>)")
            last = input("Where do you want to put it? (Your previous Schedule) :") 
            new = input("Input new schedule : ")
            day = input("Input Your Activities Day (DD/MM/YY) \t: ")
            hour = input("Input Your Activities Time (HH.MM)(24 Hour Format) \t: ")
            data = str(day)+str(" | ") + str(hour) + str(" | ") + str(new)
            tampil.AddByKey(last, data)
        
        elif action == "d":
            tampil.DeleteFirst()
            print("Schedule Has been Updated : ");tampil.display(tampil.head)

        elif action == "e":
            tampil.DeleteLast()
            print("Schedule Has been Updated : ");tampil.display(tampil.head)

        elif action == "f":
            print("Schedule : ");tampil.display(tampil.head)

            print("\nFormat Delete (DD/MM/YY | HH.MM | <Schedule that you want to delete>)")
            delete = input("Insert Schedule That You Want To Delete By Key: ")
            tampil.DeleteByKey(delete)
        
        elif action == "g":
            sort = input("Sort this Schedule? (y/n): ")
            if sort == "y":
               tampil.head = tampil.mergeSort(tampil.head)
               tampil.display(tampil.head)
            elif sort == "n":
                tampil.display(tampil.head)

        elif action == "h":
            tampil.display(tampil.head)
        
        elif action == "j":
            exit()
if __name__ == "__main__":
  while(True):
    data()
        
