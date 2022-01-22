# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
	def firstBadVersion(self, n: int) -> int:
		lower = 1
		upper = n+1
		while lower + 1 != upper:
			mid = (lower + upper) //2
			if isBadVersion(mid):
				upper = mid
			else:
				lower = mid
		if isBadVersion(lower): return lower
		return upper