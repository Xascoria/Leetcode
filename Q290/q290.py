class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pat_dict = {}
        if len(pattern) != len(s.split()): return False

        for i,j in zip(pattern, s.split()):
            if i not in pat_dict:
                if j in pat_dict.values():
                    return False
                pat_dict[i] = j
            elif pat_dict[i] != j:
                return False
        return True