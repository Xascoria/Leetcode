class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        for i in range(97,123):
            word = word.replace(chr(i), " ")

        return len({int(i)for i in word.split()})