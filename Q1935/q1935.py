class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        bl = set(brokenLetters)
        output = 0
        for word in text.split():
            for l in word:
                if l in bl:
                    break
            else: output += 1
        return output