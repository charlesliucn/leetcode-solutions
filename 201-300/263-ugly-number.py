class Solution(object):
	def isUgly(self, num):
		"""
		:type num: int
		:rtype: bool
		"""
		if num <= 0:
			return False
		else:
			for i in [2, 3, 5]:
				while num % i == 0:
					num = num/i
			if num == 1:
				return True
			else:
				return False