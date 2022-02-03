class Trie:

    def __init__(self):
        self.root = {}
        

    def insert(self, word: str) -> None:
        cur_layer = self.root
        for i in word:
            if i not in cur_layer:
                cur_layer[i] = {}
            cur_layer = cur_layer[i]
        cur_layer["@"] = None
        

    def search(self, word: str) -> bool:
        cur_layer = self.root
        for i in word:
            if i not in cur_layer:
                return False
            cur_layer = cur_layer[i]
        return "@" in cur_layer

    def startsWith(self, prefix: str) -> bool:
        cur_layer = self.root
        for i in prefix:
            if i not in cur_layer:
                return False
            cur_layer = cur_layer[i]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)