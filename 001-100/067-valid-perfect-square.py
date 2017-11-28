class Solution(object):
	def isPerfectSquare(self, num):
		"""
		:type num: int
		:rtype: bool
		"""
		if num <= 0:
			return False
		i = 1
		while num > 0:
			num -= i
			i += 2
		if num == 0:
			return True
		else:
			return False