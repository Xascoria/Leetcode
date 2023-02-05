from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pop_ptr = 0
        for i in pushed:
            stack.append(i)
            while pop_ptr != len(popped) and stack and popped[pop_ptr] == stack[-1]:
                stack.pop()
                pop_ptr += 1
        return len(stack) == 0