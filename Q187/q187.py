class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10: return []
        output = []
        freq_dict = {}
        for i in range(len(s)-9):
            section = s[i:i+10]
            if section not in freq_dict:
                freq_dict[section] = 1
            elif freq_dict[section] == 1:
                output.append(section)
                freq_dict[section] = 2
        return output