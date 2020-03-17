class MyHashSet:

    def __init__(self):
        self.values=[0]*1000000
        

    def add(self, key: int) -> None:
        self.values[key]=1

    def remove(self, key: int) -> None:
        self.values[key]=0

    def contains(self, key: int) -> bool:
        return self.values[key]==1
        """
        Returns true if this set contains the specified element
        """
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)