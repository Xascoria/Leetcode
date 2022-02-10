from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]

        for i in range(1, len(asteroids)):
            cur = asteroids[i]
            while len(stack) != 0 and (stack[-1] > 0) and (cur < 0):
                face_off = stack.pop()
                if abs(face_off) > abs(cur):
                    cur = face_off
                elif abs(face_off) < abs(cur):
                    continue
                else:
                    cur = 0
                    break
            if cur != 0:
                stack.append(cur)
        return stack

x = Solution()
print( x.asteroidCollision([5,10,-5]) )