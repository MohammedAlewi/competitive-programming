class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banneds=set()
        for b in banned:
            banneds.add(b.upper())
        freq={}
        
        new_p=[]
        word=""
        for p in paragraph:
            if p.isalnum():
                word+=p
            elif word!="":
                new_p.append(word)
                word=""
        new_p.append(word)

        for word in new_p:
            word=word.upper()
            
            if word in banneds:
                continue
            if freq.get(word)==None:
                freq[word]=1
            else:
                freq[word]+=1
               
        choosen=None
        for i in freq.keys():
            if choosen==None:
                choosen=i
            if freq[i]> freq[choosen]:
                choosen=i
                
        return choosen.lower() if choosen!=None else ""