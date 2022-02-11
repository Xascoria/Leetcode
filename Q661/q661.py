from typing import List

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        output = [[0]*len(img[0]) for _ in range(len(img))]

        for i in range(len(img)):
            for j in range(len(img[0])):
                around = []
                for cx in range(-1,2):
                    for cy in range(-1,2):
                        if 0<=i+cx<len(img) and 0<=j+cy<len(img[0]):
                            around.append( img[i+cx][j+cy] )
                print(around)
                output[i][j] = sum(around)//len(around)
        return output

x = Solution()
print( x.imageSmoother([[1,1,1],[1,0,1],[1,1,1]]) )