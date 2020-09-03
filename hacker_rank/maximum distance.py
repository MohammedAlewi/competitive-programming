class Tries:
    def __init__(self,value,end=False):
        self.val=value
        self.end=end
        self.chids={}


def add_value(value,index,trie):
    if value[index] in trie.chids:
        if index == len(value)-1:
            trie.chids[value[index]].end=True
            return 
        add_value(value,index+1,trie.chids[value[index]])
    else:
        trie.chids[value[index]]=Tries(value[index])
        if index == len(value)-1:
            trie.chids[value[index]].end=True
            return 
        add_value(value,index+1,trie.chids[value[index]])



def build_tries(values):
    trie=Tries(None)
    for value in values:
        add_value(value,0,trie)
    max_len=[0]
    ans= traverse_tries(trie,max_len)

    return max_len



def traverse_tries(tries,max_len):
    if len(tries.chids)==2:
        left= traverse_tries(tries.chids["0"],max_len)+1
        right= traverse_tries(tries.chids["1"],max_len)+1
        max_len[0]= max(max_len[0],left+right)
        return max(left,right)
    elif len(tries.chids)==1:
        return 1 + traverse_tries(tries.chids[list(tries.chids.keys())[0]],max_len)
    return 0


val=build_tries(["1110111101","11110100110","111101001111110100110","0"])

print(val)