from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            return int(not flowerbed[0]) >= n
        allowed_flowers = 0
        if len(flowerbed) >= 2 and 0 == flowerbed[0] == flowerbed[1]:
            allowed_flowers += 1
            flowerbed[0] = 1
        for i in range(1,len(flowerbed)-1):
            if 0 == flowerbed[i-1] == flowerbed[i] == flowerbed[i+1]:
                allowed_flowers += 1
                flowerbed[i] = 1
        if len(flowerbed) >= 2 and 0 == flowerbed[-1] == flowerbed[-2]:
            allowed_flowers += 1
        return allowed_flowers >= n