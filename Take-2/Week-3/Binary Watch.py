class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        times = [] 
        for i in range(num+1):
          hours = self.generate_str(i,11)
          minutes = self.generate_str(num-i,59)
          
          for hour in hours:
            for minute in minutes:
              times.append( str(hour)+":"+ "{:02d}".format(minute) )
              
        return times
        
        
    def generate_str(self,val,bound):
      possible= []
      
      for i in range(bound+1):
        rep = str(bin(i))[2:]
        
        if rep.count('1')==val:
          possible.append(i)
          
      return possible
