class Solution(object):
	def reverseVowels(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		indices = []
		vowels = []
		for i in range(len(s)):
			if self.isvowel(s[i]):
				indices.append(i)
				vowels.append(s[i])
		numvowels = len(indices)
		s = list(s)
		for i in range(numvowels):
			s[indices[i]] = vowels[numvowels-1-i]
		return "".join(s)

	def isvowel(self, c):
		return c in ['a','e','i','o','u','A','E','I','O','U']