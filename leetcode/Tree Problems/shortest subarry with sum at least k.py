
class Solution:
    def shortestSubarray(self, a, k: int) -> int:
        orignal_k=k
        a.sort()
        sums=[]
        total=0
        while k>=0:
            found=self.bin_search_max(a,0,k,len(a)-1,sums,len(a)-1)
            if found==-1:
                return -1
            k-=a[found]
            sums.append(found)
            total+=a[found]
            

        while k<0:
            found_min=self.bin_search_min(a,0,k,len(a)-1,sums)
            found_max=self.bin_search_max(a,0,k,len(a)-1,sums,len(a)-1)

            if total+a[found_min]<orignal_k and total+a[found_max]>total:
                break
            if total+a[found_min]>=orignal_k:
                found=found_min
            else: found=found_max
            sums.append(found)
            k-=a[found]
        return len(sums)
        

    def bin_search_min(self,a,l,val,r,sums,min_val=0):
        if r>=l:
            mid=(l+r)//2
            if a[mid]==val and mid not in sums:
                return mid
            elif a[mid]<val and mid not in sums:
                return self.bin_search_min(a,mid+1,val,r,sums,mid)
            elif mid not in sums:
                return self.bin_search_min(a,l,val,mid-1,sums,min_val)
        if min_val not in sums:return min_val
        return -1

    def bin_search_max(self,a,l,val,r,sums,max_val):
        if r>=l:
            mid=(l+r)//2
            if a[mid]==val and mid not in sums:
                return mid
            elif a[mid]<val and mid not in sums:
                return self.bin_search_max(a,mid+1,val,r,sums,max_val)
            elif mid not in sums:
                return self.bin_search_max(a,l,val,mid-1,sums,mid)
        if max_val not in sums:return max_val
        return -1

s=Solution()
x=s.shortestSubarray([-4,4,4,-2,-1],5)
print(x)