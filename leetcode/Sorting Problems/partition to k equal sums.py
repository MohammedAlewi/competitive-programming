class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        x=sum(nums)/k
        l=len(nums)
        found=0
        for i in range(l):
            if nums[i]-5==0:
                found+=1
            else:
                v=nums[i]-5
                if l.index(v)==-1: 
                    return False
                else: 
                    l.pop(v)
                    found+=1
        # nums=sorted(nums)
        # set_val=[]
        # length,i=len(nums)-1,0
        # values=self.reverse(nums)
        # while i+1<=len(values):
        #     print(i,values,values[i],k,set_val)
        #     if values[i]>=x:
        #         set_val.append(values[i])
        #         i+=1
        #     else:
        #         values=values[:i+1]+self.reverse(values[i+1:])
        #         values[i]+=values.pop(i+1)

                
                
        print(set_val)
        
    def reverse(self,list_val):
        x=[]
        length=len(list_val)-1
        while length>=0:
            x.append(list_val[length])
            length-=1
        return x
    
s=Solution()
s.canPartitionKSubsets([1,1,1,3,3,3,3,3,3,3,3],3)
# [1,2,2,3,3,4,5]
#     def calculate(self,nums,x,values):
#         if len(x)==0:
#             return values
#         if nums[len(nums)-1]>=x:
#             values.append([nums[len(nums)-1]])
#             return self.calculate(nums[:len(nums)-1],x,values)
#         else:
#             s=[]
#             i,j=0,0
#             while(sum[s]>=x):
#                 if i>j:
#                     j+=1
#                     s.append(nums[len(nums)-j-1])
#                 else:
#                     i+=1
#                     s.append(nums[i])
#             values.append(s)
#             return self.calculate(nums[i:j],x,values)
# # sets=[]
# # i,j=0,1
# # s=[nums[len(nums)-1]]
# # while j>=0:
# #     if sum(s)<x:
# #         index=min(i,j)
# #         s.append(nums[i])
# #         i+=1
# #     if sum(s)>=x:
# #         sets.append(s)
# #         s=[]
# #     j-=1
# #     s.append(nums[j])
# # print(sets)
# # return len(sets)==k