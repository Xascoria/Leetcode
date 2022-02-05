#1952
class Solution:
    def isThree(self, n: int) -> bool:
        def is_prime(k):
            if k == 2: return True
            if k % 2 == 0: return False
            for i in range(3, k//2+1, 2):
                if k % i == 0:
                    return False
            return True

        return n != 1 and (n**0.5).is_integer() and is_prime( int(n**0.5) )