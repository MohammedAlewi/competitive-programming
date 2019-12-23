# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.find(n,1)
    def find(self,r,l):
        if r>=l:
            mid=int((r+l)/2)
            if isBadVersion(mid):
                if isBadVersion(mid-1)==False:
                    return mid
                return self.find(mid-1,l)
            return self.find(r,mid+1)
                
            
        return mid