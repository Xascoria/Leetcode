# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
class Master:
    def guess(self, word: str) -> int:
        pass

from typing import List

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        freq_dict_arr = [{}, {}, {}, {}, {}, {}]
        def word_val(word):
            return sum( freq_dict_arr[i][word[i]] for i in range(6) )
        while True:
            freq_dict_arr = [{}, {}, {}, {}, {}, {}]
            for word in wordlist:
                for i in range(6):
                    freq_dict_arr[i][ word[i] ] = freq_dict_arr[i].get(word[i], 0) + 1
            word_to_guess = max(wordlist, key=word_val)
            out = master.guess(word_to_guess)
            if out == 6:
                break
            else:
                filtered_list = []
                for word in wordlist:
                    similar = 0
                    for i,j in zip(word_to_guess, word):
                        similar += i == j
                    if similar == out:
                        filtered_list.append( word )
                wordlist = filtered_list