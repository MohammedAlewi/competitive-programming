class Solution:
    def __init__(self):
        self.r=0
        self.b=0
        
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        queue=collections.deque()
        graph={}
        for i in red_edges:
            if graph.get(i[0])==None:
                graph[i[0]]=[[i[1]],[]]
            else:
                graph[i[0]][0].append(i[1])
        
        for i in blue_edges:
            if graph.get(i[0])==None:
                graph[i[0]]=[[],[i[1]]]
            else:
                graph[i[0]][1].append(i[1])
                
        queue.append((0,True))
        queue.append((0,False))
        distance={}
        distance[(0,True)]=0
        distance[(0,False)]=0
        
        
        while len(queue):
            node=queue.popleft()
            childrens=[]
            if graph.get(node[0])!=None:
                childrens=graph[node[0]][1] if node[1] else graph[node[0]][0]
            for child in childrens:
                if distance.get((child,not node[1]))==None:
                    distance[(child,not node[1])]=distance[node]+1
                    queue.append((child,not node[1]))
        ans=[-1]*n
        
        for i in range(n):
            left=distance.get((i,True))
            right=distance.get((i,False))
            
            if left!=None  and right!=None:
                ans[i]=min(left,right)
            elif left!=None:
                ans[i]=left
                
            elif right!=None:
                ans[i]=right
        
        
        return ans

        