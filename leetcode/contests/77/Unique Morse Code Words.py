class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        values=set()
        
        for i in words:
            morse_val=""
            for j in i:
                morse_val+=morse[ord(j)-97]
            values.add(morse_val)
        
        return len(values)