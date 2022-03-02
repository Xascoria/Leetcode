from typing import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        freq_dict = {}
        for i,j in edges:
            freq_dict[i] = freq_dict.get(i,0)+1
            freq_dict[j] = freq_dict.get(j,0)+1

        k = max(freq_dict)
        for i in freq_dict:
            if freq_dict[i] == k-1:
                return i