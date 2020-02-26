# from collections import namedtuple

# forzen = frozenset([3,4,2,2,2,23,12])
# # print(forzen)


# Point=namedtuple("Point","x y")

# p=Point(34,12)
# # print(p.x)
# # print(p.y)

# l=[1,2,3,34,5,232,12]

# for i in enumerate(l):
#     print(i)


# from itertools import *

# print(list(product([3,4],[1,2])))






class Person:

    def __init__(self,a=None):
        self.num=[a]

    def get_sex(self):
        return "sometimes...."+str(self.num[0])

    def __str__(self):
        return str(self.num[0])

class Peoples:
    def __init__(self,amount):
        self.amount=amount

    def __str__(self):
        return str(self.amount)+" peoples!!"





# @dataclass(order=False, frozen=True)
class Employee(Person,Peoples):
    # def __init__(self,a=None):
    #     super().__init__(a)
    #     self.name=None
    #     self.LastName=None

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self,name):
        self.name=name

    @property
    def lastName(self):
        return self.lastName
    
    @lastName.setter
    def lastName(self,lastName):
        self.lastName=lastName

    

# p=Person(43)
# p=Person()
# e=Employee(34)
# print(e)
# print(e.get_sex())


class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

    def __next__(self):
        self=self.next
        return self.next

    def __eq__(self,other):
        return  self.val == other.val

    def __ne__(self,other):
        return self.val != other.val

    def __lt__(self,other):
        return self.val < other.val

    def __gt__(self,other):
        return self.val > other.val

    def __le__(self,other):
        return self.val <= other.val

    def __ge__(self,other):
        return self.val >= other.val

    def __hash__(self):
        return hash(self.val)

    def __repr__(self):
        return str(self.val)

    def __iter__(self):
        self=self.next
        return self

    def __len__(self):
        return 1

l=Node(43)
l.next=Node(12)

l.next.next=Node(32)

# print(l)
# print(l!=c)
# print(l)

for i in l:
    print(l)