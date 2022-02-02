from typing import List

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(map(str.count(" ")+1,sentences))
