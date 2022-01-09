from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr = []
        for i in range(1, n+1):
            out=""
            if i%3 == 0:out += "Fizz"
            if i%5 == 0:out += "Buzz"
            if out:
                arr.append(out)
            else:
                arr.append(i)
        return arr