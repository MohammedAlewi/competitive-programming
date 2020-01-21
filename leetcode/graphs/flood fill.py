class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        reach=[]
        reach.append((sr,sc))
        neb=[(0,1),(0,-1),(-1,0),(1,0)]
        
        explored={}
        
        while(len(reach)>0):
            sr,sc=reach.pop(0)
            for n in neb:
                row,col=sr+n[0],sc+n[1]
                if row >= len(image) or col >=len(image[0]) or row<0 or col<0:
                    continue
                elif image[sr][sc]==image[row][col] and explored.get(str(sr)+str(sc))==None :
                    reach.append((row,col))
                    
            image[sr][sc]=newColor
            explored[str(sr)+str(sc)]=True
        return image