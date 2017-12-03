class Solution(object):
	def monotoneIncreasingDigits(self, N):
		"""
		:type N: int
		:rtype: int
		"""
		n = N
		bits = ""
		while True:
			if n == 0:
				break
			n, r = divmod(n, 10)
			bits = bits + str(r)
		bits = bits[::-1]
		bitnum = len(bits)
		print(bits)
		print(bitnum)
		res = ""
		for i in range(bitnum):
			if int(bits[i:]) >= int(bits[i])*int("".join(['1']*(bitnum-i))):
				res = res+bits[i]
			else:
				res = res+str(int(bits[i])-1)
				res = res+'9'*(bitnum-i-1)
				break
		return int(res)

if __name__ == '__main__':
	print(Solution().monotoneIncreasingDigits(2014011216))



