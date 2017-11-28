class Solution(object):
	def constructRectangle(self, area):
		"""
		:type area: int
		:rtype: List[int]
		"""
		if area == 0:
			return [0,0]
		if area == 1:
			return [1,1]
		import math
		bound = int(math.sqrt(area))
		w = 0
		for i in range(1, bound+1):
			if area % i == 0:
				w = i
		return [area//w, w]

# if __name__ == '__main__':
# 	t = Solution()
# 	for i in range(100):
# 		s = t.constructRectangle(i)
# 		print([i,s])