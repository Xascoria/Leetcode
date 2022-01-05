from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # charset = set()
        # for i in wordDict:
        #     charset |= set(i)
        # sset = set(s)
        # if sset & charset != sset:
        #     return False

        processed_dict = {}
        for i in wordDict:
            if len(i) not in processed_dict:
                processed_dict[len(i)] = set([i])
            else:
                processed_dict[len(i)].add(i)
        longest_fst = sorted(processed_dict.keys(),reverse=1)
        recursion_cache = set()

        def recursion(current_index):
            if current_index == len(s):
                return True
            if current_index in recursion_cache:
                return False

            for length in longest_fst:
                if len(s) - current_index < length:
                    continue
                if s[current_index:current_index+length] in processed_dict[length]:
                    if recursion(current_index+length):
                        return True

            recursion_cache.add(current_index)
            return False
        
        return recursion(0)

x = Solution()
print( x.wordBreak("abcd",["a","abc","b","cd"]) )