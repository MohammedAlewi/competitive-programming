class ProductOfNumbers:

    def __init__(self):
        self.values=[1]
        self.counter=0
        self.zeros=[]
        
    def add(self, num: int) -> None:
        if num==0:
            self.zeros.append(self.counter)
            self.values.append(1)
        else:
            new=self.values[-1]*num
            self.values.append(new)
        self.counter+=1

    def getProduct(self, k: int) -> int:
        if self.get_mid_zero(k):
            return 0
        
        last=self.values[-1]
        kth=self.values[len(self.values)-1-k]
        # print(self.values,last,kth,k)
        return last//kth
        
    def get_mid_zero(self,k):
        for i in self.zeros:
            if self.counter-k-1 < i:
                return True
        return False


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)