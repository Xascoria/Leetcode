from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        zero_b4 = 0
        total = 0
        for row in bank:
            if "1" in row:
                one_count = row.count("1")
                total += one_count * zero_b4
                zero_b4 = one_count
        return total