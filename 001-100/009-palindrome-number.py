class Solution(object):
	def isPalindrome(self, x):
		"""
		:type x: int
		:rtype: bool
		"""
		if x < 0:
			return False
		if x == 0:
			return True
		num = x
		bits = []
		while True:
			if num == 0:
				break
			num, rem = divmod(num, 10)
			bits.append(rem)
		start = 0
		end = len(bits) - 1
		while start <= end:
			if bits[start] == bits[end]:
				start += 1
				end -= 1
			else:
				return False
		return True