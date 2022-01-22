class Solution:
	def winnerSquareGame(self, n: int) -> bool:
		arr = [False] * (n+1)
		arr[1] = True
		ptr_arr = [1]
		for i in range(2, n+1):
			if (i**0.5).is_integer():
				arr[i] = True
				ptr_arr.append(0)
			else:
				# if all([arr[ptr] for ptr in ptr_arr]):
				# 	arr[i] = False
				# else:
				# 	arr[i] = True
				for ptr in ptr_arr:
					if not arr[ptr]:
						arr[i] = True
						break
				else:
					arr[i] = False
			ptr_arr = [i+1 for i in ptr_arr]
		#print(arr)
		return arr[-1]

x = Solution()
print( x.winnerSquareGame(6) )