"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""
class Solution(object):
    def findSolution(self, customfunction, z):
        func=customfunction
        x,y=1,1
        ans=[]
        while(x<1000):
            y=1
            while(y<1000  and func.f(x,y)<=z):
                if func.f(x,y)==z:
                    ans.append([x,y])
                y+=1
            x+=1
        return ans
            
        """
        :type num: int
        :type z: int
        :rtype: List[List[int]]
        """
        