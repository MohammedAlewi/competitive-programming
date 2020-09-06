class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        taken =set()
        length=len(flowerbed)
        for i in range(length):
            if flowerbed[i]==flowerbed[max(i-1,0)]==flowerbed[min(i+1,length-1)]==0:
                flowerbed[i]=1
                n= max(n-1,0)
        return n==0
