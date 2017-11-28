class Solution(object):
	def checkRecord(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		count1 = 0
		for i in range(len(s)):
			if s[i] == 'A':
				count1 += 1
				if count1 > 1:
					return False
			elif s[i] == 'L':
				if i < len(s) - 2:
					if s[i+1] == 'L' and s[i+2] == 'L':
						return False
		return True
