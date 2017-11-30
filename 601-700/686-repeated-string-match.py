class Solution(object):
	def repeatedStringMatch(self, A, B):
		"""
		:type A: str
		:type B: str
		:rtype: int
		"""
		a = set(A)
		b = set(B)
		if not b.issubset(a):
			return -1
		if B in A:
			return 1
		if A not in B:
			return -1
		Alen = len(A)
		Blen = len(B)
		mint = len(B)//len(A)
		i = mint
		tmp = A*(i-1)
		while True:
			tmp = tmp + A
			if B in tmp:
				return i
			if len(tmp) > len(B) + len(A):
				return -1
			i += 1
