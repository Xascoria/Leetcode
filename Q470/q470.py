# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
	def rand10(self):
		"""
		:rtype: int
		"""
		initial = rand7()
		while initial == 4:
			initial = rand7()
		using_fh = initial < 4
		val = rand7()
		while val >= 6:
			val = rand7()
		if using_fh:
			return val
		return val+5