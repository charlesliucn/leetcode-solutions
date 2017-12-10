class Solution(object):
	def nextGreatestLetter(self, letters, target):
		"""
		:type letters: List[str]
		:type target: str
		:rtype: str
		"""
		letterlen = len(letters)
		if ord(target) >= ord(letters[letterlen-1]):
			return letters[0]
		if ord(target) < ord(letters[0]):
			return letters[0]
		for i in range(letterlen-1):
			if ord(letters[i]) <= ord(target) and ord(letters[i+1]) > ord(target):
				return letters[i+1]