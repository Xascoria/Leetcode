class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n % 2:
            return range(-n//2+1, n//2+1)
        else:
            return [*range(1,n//2+1), *range(-1,-n//2-1,-1)]