from math import sqrt
class Solution(object):
	def judgeSquareSum(self, c):
		"""
		:type c: int
		:rtype: bool
		"""
		flags = self.is_square(c - a*a) for a in range(int(sqrt(c)) + 1)
		return any(flags)
	
	def is_square(self, N):
		return int(sqrt(N))**2 == N