class Solution:
	def numSquares(self, n: int) -> int:
		arr = [0] * (n+1)
		arr[1] = 1
		ptr_arr = [1]
		for i in range(2, n+1):
			if (i**0.5).is_integer():
				arr[i] = 1
				ptr_arr.append(0)
			else:
				arr[i] = min([arr[ptr] for ptr in ptr_arr])+1
			ptr_arr = [i+1 for i in ptr_arr]
		return arr[-1]