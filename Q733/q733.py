from typing import List

class Solution:

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor: return image
        queue = {(sr,sc)}
        old_color = image[sr][sc]
        trans = ((-1,0),(1,0),(0,-1),(0,1))
        while queue:
            cx, cy = queue.pop()
            for i,j in trans:
                if 0<=cx+i<len(image) and 0<=cy+j<len(image[0]) and image[cx+i][cy+j] == old_color and (cx+i, cy+j)not in queue:
                    queue.add( (cx+i, cy+j) )
            image[cx][cy] = newColor
        return image

x = Solution()
a = [[0,0,0],[0,1,1]]
b = 1
c = 1
d = 1
print( x.floodFill(a,b,c,d) )