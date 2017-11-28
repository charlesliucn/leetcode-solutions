class Solution(object):
	def findContentChildren(self, g, s):
		"""
		:type g: List[int]
		:type s: List[int]
		:rtype: int
		"""
		g = sorted(g)
		s = sorted(s)
		numfind = 0
		if len(g) == 0:
			return 0
		try:
			for i in g:
				s.remove(self.firstGreater(s, i))
				print(s)
				numfind += 1
			return numfind
		except ValueError:
			return numfind

	def firstGreater(self, list_a, num):
		for i in list_a:
			if i >= num:
				return i

if __name__ == '__main__':
	t = Solution()
	print(t.findContentChildren([10,9,8,7],[10,9,8,7]))