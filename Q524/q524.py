from typing import List

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        main_dict = {chr(i+97):set() for i in range(26)}
        for word in dictionary:
            main_dict[word[0]].add( (0, word) )
        cur_length = 0
        cur_output = ''

        for char in s:
            to_process_set = main_dict[char]
            main_dict[char] = set()

            for i,j in to_process_set:
                if i+1 == len(j):
                    if i+1 > cur_length:
                        cur_length = i+1
                        cur_output = j
                    elif i+1 == cur_length and j<cur_output:
                        cur_output = j
                        
                else:
                    nc = i+1
                    main_dict[j[nc]].add( (nc,j) )
            
        return cur_output
        


x = Solution()
print( x.findLongestWord("abpcplea", dictionary = ["ale","apple","monkey","plea"]) )