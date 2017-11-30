class Solution(object):
	def isIsomorphic(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: bool
		"""
		if len(s) != len(t):
			return False
		return self.isIsomorphic_single(s,t) and self.isIsomorphic_single(t,s)
	def isIsomorphic_single(self, s, t):
		res = {}
		slen = len(s)
		for i in range(slen):
			if s[i] not in res:
				res[s[i]] = t[i]
			elif res[s[i]] != t[i]:
				return False
		return True


if __name__ == '__main__':
	print(Solution().isIsomorphic("ab","aa"))