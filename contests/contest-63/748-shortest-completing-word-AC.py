from collections import Counter
class Solution(object):
	def shortestCompletingWord(self, licensePlate, words):
		"""
		:type licensePlate: str
		:type words: List[str]
		:rtype: str
		"""
		minlen = 10000
		res = None
		licensePlate = licensePlate.lower()
		alphas = [c for c in licensePlate if c.isalpha()]
		print(alphas)
		for s in words:
			if self.scramble(s, alphas):
				tmp = s
				if len(tmp) < minlen:
					res = tmp
					minlen = len(tmp)
		return res

	def scramble(self, s1, s2):
		return len(Counter(s2) - Counter(s1)) == 0