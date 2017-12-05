class Solution(object):
	def longestCommonPrefix(self, strs):
		"""
		:type strs: List[str]
		:rtype: str
		"""
		if strs == []:
			return ""
		lens = [len(s) for s in strs]
		slen = min(lens)
		strslen = len(strs)
		j = 0
		res = ""
		while j < slen:
			count = 0
			for i in range(1, strslen):
				if strs[i][j] == strs[0][j]:
					count += 1
				else:
					return res
			if count == strslen - 1:
				res = res + strs[0][j]
				j += 1
		return res