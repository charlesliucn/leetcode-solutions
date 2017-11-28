class Solution(object):
	def repeatedSubstringPattern(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		strlen = len(s)
		for i in range(1, strlen//2+1):
			if strlen % i == 0:
				if s == s[:i]*(strlen/i):
					return True
		return False