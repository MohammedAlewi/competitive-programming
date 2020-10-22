from collections import defaultdict
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        result = []
        values = defaultdict(lambda:[])
        
        for i in range(len(groupSizes)):
            values[ groupSizes[i] ].append(i)
            
            if len( values[ groupSizes[i] ] ) ==  groupSizes[i]:
                result.append( values[ groupSizes[i] ] )
                values[ groupSizes[i] ] = []
                
        return result
        
