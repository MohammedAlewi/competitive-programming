class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        memory = {}
        def make_sentences(start):
            nonlocal s, words, memory
            if start >= len(s):
                return [""]
            if start in memory:
                return memory[start]
            
            results = []
            for end in range(start, len(s) + 1):
                string = s[start : end]
                if string in words:
                    res = make_sentences(end)
                    for r in res:
                        end = " " + r if r else r
                        results.append((string + end).strip())
            
            memory[start] = results
            return memory[start]
        return make_sentences(0)
