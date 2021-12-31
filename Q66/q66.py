class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry_over = 1
        for i in range(len(digits)-1, -1, -1):
            digits[i] += carry_over
            if digits[i] == 10:
                carry_over = 1
                digits[i] = 0
            else:
                carry_over = 0
                break
        if carry_over:
            return [1] + digits
        return digits
            