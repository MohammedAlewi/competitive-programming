import collections
class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        if len(A)<2:
            return False
        A.sort()
        
        totalAve=sum(A)
        
        end_state=set()
        final_level=0
        for i in range(1,int(len(A)//2+1)):
            if (i*totalAve)%len(A)==0:
                end_state.add((i*totalAve//len(A),i))
                end_state.add(((len(A)-i)*totalAve//len(A),(len(A)-i)))
                final_level=max(final_level,i)
        
        visited={}
        queue=collections.deque()
        queue.append((0,0))
        visited[(0,0)]=set()
        while len(queue):
            node=queue.popleft()
            childs=visited[node]
            currents=set()
            for i in range(len(A)):
                if i in childs:
                    continue
                new_node=node[0]+A[i],node[1]+1
                if new_node in currents:
                    continue
                currents.add(new_node)
                if new_node in end_state:
                    return True
                if new_node not in childs and new_node[1]<=final_level and visited.get(new_node)==None:
                    queue.append(new_node)
                    visited[new_node]=self.new_set(childs,i)
        return False
                    
                    
    def new_set(self,old_set,new_element):
        new=set()
        for i in old_set:
            new.add(i)
        new.add(new_element)
        return new
                    
            
        
                