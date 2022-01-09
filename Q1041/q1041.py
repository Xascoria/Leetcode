class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = 0
        trans = ((0, -1), (1, 0), (0, 1), (-1, 0))
        cur_x = cur_y = 0
        for i in instructions:
            if i == "R":
                direction += 1
                if direction == 4:
                    direction = 0
            elif i == "L":
                direction -= 1
                if direction == -1:
                    direction = 3
            else:
                cur_x += trans[direction][0]
                cur_y += trans[direction][1]

        if direction == 0:
            return cur_x == cur_y == 0
        return True

x = Solution()
print( x.isRobotBounded("GL") )