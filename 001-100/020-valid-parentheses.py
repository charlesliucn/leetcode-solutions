class Solution(object):
	def isValid(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		stack = []
		dic = {']':'[', '}':'{', ')':'('}
		for c in s:
			if c in dic.values():
				stack.append(c)
			elif c in dic.keys():
				if stack == [] or stack.pop() != dic[c]:
					return False
			else:
				return False
		return stack == []