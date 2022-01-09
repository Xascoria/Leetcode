from _typeshed import ReadOnlyBuffer


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        mag_dict = {}
        for i in magazine:
            if i not in mag_dict:
                mag_dict[i] = 1
            else:
                mag_dict[i] += 1
        ran_dict = {}
        for i in ransomNote:
            if i not in ran_dict:
                ran_dict[i] = 1
            else:
                ran_dict[i] += 1

        for i in ran_dict:
            if i not in mag_dict: 
                return False
            if ran_dict[i] > mag_dict[i]:
                return False
        return True
