class Codec:
    def __init__(self):
        self.encoded=dict()
        self.decoded=dict()
        self.counter=0
        self.starter='http://tinyurl.com/'

    def encode(self, longUrl: str) -> str:
        if longUrl not in self.encoded:
            self.encoded[longUrl]=self.starter+str(self.counter)
            self.decoded[self.starter+str(self.counter)]=longUrl
            self.counter+=1
        return self.encoded[longUrl]

    def decode(self, shortUrl: str) -> str:
        if shortUrl in self.decoded:
            return self.decoded[shortUrl]
        return None


# # Your Codec object will be instantiated and called as such:
# codec = Codec()
# url="https://leetcode.com/problems/design-tinyurl"
# res=codec.decode(codec.encode(url))
# print(res,"     ", codec.encode(url))