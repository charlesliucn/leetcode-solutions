class Solution:
	def isPowerOfFour(self, num):
		"""
		:type num: int
		:rtype: bool
		"""
		if  num & (num - 1):
			return False
		flag = num & 0x55555555
		if flag:
			return True
		else:
			return False