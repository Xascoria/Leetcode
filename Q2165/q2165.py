class Solution:
    def smallestNumber(self, num: int) -> int:
        zarr = []
        other_arr = []
        for i in str(num):
            if i != "0":
                other_arr.append(i)
            else:
                zarr.append(i)
        if not other_arr:
            return 0
        other_arr.sort()
        if other_arr[0] != "-":
            return int( other_arr[0] + ''.join(zarr + other_arr[1:]) )
        return -int(''.join(other_arr[1:][::-1] + zarr))

x = Solution()
print( x.smallestNumber(-7650) )