from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        prev_index = 0
        cur_length = 0
        output = []
        for cur_index in range(len(words)):
            cur_length += len(words[cur_index]) + 1
            if cur_length - 1 > maxWidth:

                words_lengths = cur_length - 1 - len(words[cur_index]) - cur_index + prev_index
                spaces_needed = max(cur_index - prev_index - 1,1)
                spaces_lengths = maxWidth - words_lengths
                spaces = [spaces_lengths//spaces_needed*" "for _ in range(spaces_needed)]+[""]
                if spaces_needed > 0:
                    for i in range(spaces_lengths%spaces_needed):
                        spaces[i] += " "
                newline = ""
                for i,j in zip(words[prev_index:cur_index],spaces):
                    newline+=i+j
                output.append(newline)
                cur_length = len(words[cur_index]) + 1
                prev_index = cur_index
        return output + [" ".join(words[prev_index:]).ljust(maxWidth)]

x = Solution()
print( x.fullJustify(["What","must","be","acknowledgment","shall","be"],16) )