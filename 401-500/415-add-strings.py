class Solution(object):
	def addStrings(self, num1, num2):
		"""
		:type num1: str
		:type num2: str
		:rtype: str
		"""
		res = ""
		carry = 0
		numlen1 = len(num1)
		numlen2 = len(num2)
		if numlen1 > numlen2:
			maxLen = numlen1
			numcom = '0'*(numlen1 - numlen2)
			num2 = numcom + num2
		else:
			maxLen = numlen2
			numcom = '0'*(numlen2 - numlen1)
			num1 = numcom + num1
		for i in range(1, maxLen+1):
			bitsum = int(num1[-i]) + int(num2[-i]) + carry
			carry = bitsum // 10
			res = str(bitsum % 10) + res
		if carry:
			res = str(carry) + res
		return res

if __name__ == '__main__':
	t = Solution()
	print(t.addStrings('67892','48229'))