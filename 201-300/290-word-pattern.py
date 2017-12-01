class Solution(object):
	def wordPattern(self, pattern, str):
		"""
		:type pattern: str
		:type str: str
		:rtype: bool
		"""
		elements = str.split()
		strlen = len(elements)
		if strlen != len(pattern):
			return False
		return self.isIsomorphic(pattern, elements, strlen) and self.isIsomorphic(elements, pattern, strlen)

	def isIsomorphic(self, pattern, elements, slen):
		res = {}
		for i in range(slen):
			if pattern[i] not in res:
				res[pattern[i]] = elements[i]
			elif res[pattern[i]] != elements[i]:
				return False
		return True


if __name__ == '__main__':
	print(Solution().wordPattern("abba","dog cat cat dog"))