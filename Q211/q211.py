class WordDictionary:
    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        cur_dict = self.root
        for i in word:
            if i not in cur_dict:
                cur_dict[i] = {}
            cur_dict = cur_dict[i]
        cur_dict["@"] = {}
        

    def search(self, word: str) -> bool:
        def recursion(cur_dict, index):
            #print(cur_dict, index)
            if index == len(word):
                return "@" in cur_dict
            
            if word[index] == ".":
                if len(cur_dict) > 0:
                    for i in cur_dict:
                        if recursion(cur_dict[i], index+1):
                            return True
                    return False
                else:
                    return False
            
            if word[index] in cur_dict:
                return recursion(cur_dict[word[index]], index+1)
            return False
        return recursion(self.root, 0)
        
x = WordDictionary()
x.addWord("a")
x.addWord("ab")
print(x.search("a."))


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)