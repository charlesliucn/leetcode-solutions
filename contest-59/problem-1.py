class Solution(object):
	def selfDividingNumbers(self, left, right):
		"""
		:type left: int
		:type right: int
		:rtype: List[int]
		"""
		res = []
		for i in range(left,right+1):
			if self.isselfDividing(i):
				res.append(i)
		return res


	def isselfDividing(self, num):
		bits = []
		x = num
		while True:
			if x == 0:
				break
			x, rem = divmod(x, 10)
			bits.append(rem)
		print(bits)
		for i in bits:
			if i == 0:
				return False
			if i != 0 and num % i != 0:
				return False
		return True

if __name__ == '__main__':
	t = Solution()
	print(t.selfDividingNumbers(1,22))