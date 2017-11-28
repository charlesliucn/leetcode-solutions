class Solution(object):
	def countAndSay(self, n):
		"""
		:type n: int
		:rtype: str
		"""
		res = "1"
		for i in range(n-1):
			res = self.Say(res)
		return res

	def Say(self, string):
		say = ""
		count = 1
		slen = len(string)
		if slen == 1:
			say = say + str(count)
			say = say + str(string[0])
		else:
			for i in range(1, slen):
				if string[i] == string[i-1]:
					count += 1
				else:
					say = say + str(count)
					say = say + str(string[i-1])
					count = 1
			say = say + str(count)
			say = say + str(string[slen-1])
		return say

if __name__ == '__main__':
	t = Solution()
	print(t.countAndSay(5))