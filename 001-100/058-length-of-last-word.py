class Solution(object):
	def lengthOfLastWord(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		slen = len(s)
		res = 0
		index = slen - 1
		for i in range(slen):
			if s[slen-1-i] == " ":
				index -= 1
			else:
				break
		for i in range(index+1):
			if s[index-i] != " ":
				res += 1
			else:
				break
		return res