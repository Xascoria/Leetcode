from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n):
            for j in range(n-i):
                a,b = n-j-1,n-i-1
                matrix[i][j],matrix[a][b] = matrix[a][b],matrix[i][j]

        for i in range(len(matrix)//2):
            matrix[i], matrix[-1-i] = matrix[-1-i], matrix[i]
            
x = Solution()

m = []
for i in range(5):
    m += [[i+j*2 for j in range(5)]]
for i in m:
    print(i)
print('e')
x.rotate(m)