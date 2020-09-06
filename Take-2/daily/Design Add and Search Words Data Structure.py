from collections import defaultdict

class WordDictionary:

    def __init__(self):
        self.tries=Trie()
        

    def addWord(self, word: str) -> None:
        res=self.insertLetter(word,0,self.tries)
        
    def insertLetter(self,word,index,trie):
        if index < len(word):
            if word[index]  not in trie.values:
                trie.values[word[index]]=Trie()
            return self.insertLetter(word,index+1,trie.values[word[index]])               
        trie.end=True
        return trie

    
    def search(self, word: str) -> bool:
        return self.searchHelper(word,0,self.tries)
        
    def searchHelper(self,word,index,trie):
        if index == len(word):
            return trie.end
        
        elif word[index] == '.':
            result = False
            for key in trie.values.keys():
                r = self.searchHelper(word,index+1,trie.values[key])
                result = result or r
            return result
        
        elif word[index] in trie.values:
            return self.searchHelper(word,index+1,trie.values[ word[index] ])
        else:
            return False
           
            
            
class Trie:
    def __init__(self):
        self.values={}
        self.end=False
    def __str__(self):
        print(self.values)
        return str(self.end)
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
