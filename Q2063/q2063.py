class Solution:
    def countVowels(self, word: str) -> int:
        alpha = set("aeiou")
        output = 0
        for i in range(len(word)):
            if word[i] in alpha:
                output += (i+1)*(len(word)-i)
        return output