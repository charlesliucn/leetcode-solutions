from collections import Counter
class Solution(object):
	def findAnagrams(self, s, p):
		"""
		:type s: str
		:type p: str
		:rtype: List[int]
		"""
		res = []
		slen, plen = len(s), len(p)
		if len(s) < len(p):
			return res
		pCounter = Counter(p)
		sCounter = Counter(s[:plen-1])
		i = 0
		while i < slen-plen:
			sCounter[s[i+plen-1]] += 1
			if sCounter == pCounter:
				res.append(i)
			sCounter[s[i]] -= 1
			if sCounter[s[i]] == 0:
				del sCounter[s[i]]
			i += 1
		return res
# if __name__ == '__main__':
# 	print(Solution().findAnagrams("cbaebabacdds","abc"))