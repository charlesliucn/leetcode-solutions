class Solution(object):
	def isAnagram(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: bool
		"""
		alphabet = [0]*26
		for c in s:
			alphabet[ord(c)-ord('a')] += 1
		for c in t:
			alphabet[ord(c)-ord('a')] -= 1
		for i in alphabet:
			if i != 0:
				return False
		return True

if __name__ == '__main__':
	t = Solution()
	print(t.isAnagram("",""))