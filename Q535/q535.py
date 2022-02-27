class Codec:
    def __init__(self):
        self.link_to_num = {}
        self.num_to_link = {}
        self.cur_num = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl in self.link_to_num:
            return self.link_to_num[longUrl]
        
        self.link_to_num[longUrl] = str(self.cur_num)
        self.num_to_link[str(self.cur_num)] = longUrl
        self.cur_num += 1
        return self.link_to_num[longUrl]
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.num_to_link[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))