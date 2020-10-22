class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        result = [None]*len(people)
        
        people.sort(key = lambda val:val[0])
        
        for i in people:
            count,j = 0,0
            while count < i[1]:
                if result[j] == None or result[j][0] >= i[0]:
                    count += 1
                j += 1
            
            while result[j] != None:
                j += 1
                
            result[j] = i
            
        return result
            
