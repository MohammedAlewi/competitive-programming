class MyCircularDeque:
    def __init__(self, k: int):
        self.size=k
        self.index=0
        self.head=Node(None)
        self.tail=self.head

    def insertFront(self, value: int) -> bool:
        if self.index==self.size: return False
        n=Node(value)
        if self.index==0:
            self.head=n
            self.head.prev=self.head
            n.prev=self.head
            self.tail=n
        else:
            self.head.prev=n
            n.next=self.head
            self.head=n
            self.head.prev=self.head
        self.index+=1
        return True

    def insertLast(self, value: int) -> bool:
        if self.index==self.size: return False
        n=Node(value)
        if self.index==0:
            self.head=n
            self.head.prev=self.head
            self.tail=n
            self.tail.prev=self.head
        else:
            n.prev=self.tail
            self.tail.next=n
            self.tail=n
        self.index+=1
        return True

    def deleteFront(self) -> bool:
        if self.index==0: return False
        self.head.prev=self.head.next
        self.head=self.head.next
        self.index-=1
        return True

    def deleteLast(self) -> bool:
        if self.index==0: return False
        self.tail=self.tail.prev

        self.index-=1
        return True

    def getFront(self) -> int:
        if self.index==0: return -1
        return self.head.val

    def getRear(self) -> int:
        if self.index==0: return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        return self.index==0

    def isFull(self) -> bool:
        return self.index==self.size

    
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None



n= MyCircularDeque(1000)
l=[]
for i in l:
    n.insertFront(i)

print(n.getFront())
print(n.getRear())
for i in l:
    if(n.getRear()!=i):
        print(n.getRear(),i)
        print(False)
        break
    n.deleteLast()
print(True)

# print("Insert Front :",n.insertFront(3))
# # print("Insert Last :",n.insertLast(4))
# print("Insert Front :",n.insertFront(1))
# print("Insert Front :",n.insertFront(2))
# # print("Insert Last :",n.insertLast(6))
# # print("Insert Last :",n.insertLast(7))

# n.printer()

# # print("Is Empty :",n.isEmpty())
# # print("Is Full :",n.isFull())

# print("Get Front :",n.getFront())
# print("Get Last :",n.getRear())

# print("delete Last :",n.deleteLast())
# # print("delete firts :",n.deleteFront())

# n.printer()

# print("Get Front :",n.getFront())
# print("Get Last :",n.getRear())
# print("delete Last :",n.deleteLast())
# # print("delete firts :",n.deleteFront())

# n.printer()

# print("Get Front :",n.getFront())
# print("Get Last :",n.getRear())

# print("delete firts :",n.deleteFront())
# # print("delete Last :",n.deleteLast())

# print("delete Last :",n.deleteLast())
# print("delete Last :",n.deleteFront())


# n.printer()
# print("Get Front :",n.getFront())
# print("Get Last :",n.getRear())

# # print("delete firts :",n.deleteFront())
# # print("delete firts :",n.deleteFront())


# # print("Get Front :",n.getFront())
# # print("Get Last :",n.getRear())

# # print("delete firts :",n.deleteFront())

# # print("Is Empty :",n.isEmpty())
# # print("Is Full :",n.isFull())