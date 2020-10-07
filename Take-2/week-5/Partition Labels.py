class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        pos = {}
            
        for i in range(len(S)):
            if S[i] in pos:
                pos[ S[i] ][1] = i
            else:
                pos[ S[i] ] = [i,i]
                
        positions = sorted(pos.values(),key=lambda val:val[0])
        
        partition = []
        c,r = 0,1 
        l = positions[0][1]
        
        while r < len(positions):
            if l < positions[r][0]:
                
                partition.append( l - c + 1 )
                c = positions[r][0]
              
            l = max(l,positions[r][1])
            r+=1
            
        partition.append(l - c + 1)
        
        return partition
