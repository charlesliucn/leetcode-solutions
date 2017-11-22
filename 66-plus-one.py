class Solution(object):
	def plusOne(self, digits):
		"""
		:type digits: List[int]
		:rtype: List[int]
		"""
		if digits == []:
			return [1]
		res = []
		realsum = digits[-1] + 1
		bitsum = realsum % 10
		carry = realsum // 10
		res.append(bitsum)
		for i in digits[:-1][::-1]:	
			realsum = i + carry
			bitsum = realsum % 10
			carry = realsum // 10
			res.append(bitsum)
		if carry == 1:
			res.append(carry)
		return res[::-1]