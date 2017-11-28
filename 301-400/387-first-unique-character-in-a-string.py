class Solution(object):
	def firstUniqChar(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		from collections import Counter
		table = Counter(s)
		for i in range(len(s)):
			if table[s[i]] == 1:
				return i
		return -1