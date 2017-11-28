class Solution:
	def findWords(self, words):
		"""
		:type words: List[str]
		:rtype: List[str]
		"""
		r = []
		for s in words:
			print(s)
			if self.isinarow(s.lower()):
				r.append(s)
		return r

	def isinarow(self, word):
		row1 = ['q','w','e','r','t','y','u','i','o','p']
		row2 = ['a','s','d','f','g','h','j','k','l']
		row3 = ['z','x','c','v','b','n','m']
		flag = 1
		if word[0] in row1:
			for i in word:
				if i not in row1:
					flag = 0
		elif word[0] in row2:
			for i in word:
				if i not in row2:
					flag = 0			
		elif word[0] in row3:
			for i in word:
				if i not in row3:
					flag = 0
		return flag