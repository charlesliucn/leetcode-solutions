class Solution(object):
	def dailyTemperatures(self, temperatures):
		"""
		:type temperatures: List[int]
		:rtype: List[int]
		"""
		lens = len(temperatures)
		res = []
		maximum = 0
		for i in range(lens):
			flag = 0
			if temperatures[i] == maximum:
				res.append(0)
			if i > 0 and temperatures[i] == temperatures[i-1]:
				if res[-1] == 0:
					res.append(0)
				else:
					res.append(res[-1]-1)
			else:
				for j in range(i+1, lens):
					if temperatures[j] > temperatures[i]:
						res.append(j-i)
						flag = 1
						break
				if flag == 0:
					res.append(0)
					maximum = temperatures[i]
		return res
if __name__ == '__main__':
	print(Solution().dailyTemperatures([34,80,80,34,34,80,80,80,80,34]))
