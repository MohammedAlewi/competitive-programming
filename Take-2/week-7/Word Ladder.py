from collections import defaultdict,deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        child = self.children(wordList)
    
        visited = {beginWord:1}
        queue = deque([beginWord])
        
        while len(queue):
            curr = queue.popleft()
            
            for word in child[curr]:
                if word == endWord:
                    return visited[curr] + 1
                if word not in visited:
                    queue.append(word)
                    visited[word] = visited[curr] + 1
        
        return 0
                    
            
        
        
        
    def children(self,wordList):
        child = defaultdict(lambda:[])
        
        contain = set(wordList)
        
        for i in range(len(wordList)):
            for j in range(97, 97+26):
                for x in range(len(wordList[i])+1):
                    word = wordList[i][:x] + str(chr(j)) + wordList[i][x+1:] 
                    if word in contain:
                        child[wordList[i]].append(word)
                
        return child
        
        
                    
            
                
