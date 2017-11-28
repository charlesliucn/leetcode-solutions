class Solution(object):
	def convertToBase7(self, num):
		"""
		:type num: int
		:rtype: str
		"""
		if num < 0:
			return "-" + self.convertToBase7Pos(-num)
		elif num > 0:
			return self.convertToBase7Pos(num)
		else:
			return "0"

	def convertToBase7Pos(self, posnum):
		base7 = ""
		while True:
			if posnum == 0: 
				break
			posnum, rem = divmod(posnum, 7)
			base7 = str(rem) + base7
		return base7
