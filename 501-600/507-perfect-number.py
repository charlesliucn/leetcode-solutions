class Solution(object):
	def checkPerfectNumber(self, num):
		"""
		:type num: int
		:rtype: bool
		"""
		fac = [x for x in self.factors(num)]
		if sum(fac) == 2 * num:
			return True
		else:
			return False

	def factors(self, n):
		k = 1
		while k * k < n:
			if n % k == 0:
				yield k
				yield n // k
			k += 1
		if k * k == n:
			yield k