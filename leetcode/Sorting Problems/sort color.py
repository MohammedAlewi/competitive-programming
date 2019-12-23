class Solution:
    def sortColors(self, nums: List[int]) -> None:
        sorted_list=[0]*(2+1)
        for i in nums: sorted_list[i]+=1
        nums.clear()
        for i in range(len(sorted_list)):
            for j in range(0,sorted_list[i]):
                nums.append(i)
        