class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        occurance = [0] * 26
        for i in s:
            occurance[ord(i)-97] += 1
        if 0 in occurance:
            return len(set(occurance)) <= 2
        else:
            return len(set(occurance)) == 1