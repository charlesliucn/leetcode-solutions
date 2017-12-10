class WordFilter(object):

	def __init__(self, words):
		"""
		:type words: List[str]
		"""
		self.words = words

	def f(self, prefix, suffix):
		"""
		:type prefix: str
		:type suffix: str
		:rtype: int
		"""
		index = -1
		prelen = len(prefix)
		suflen = len(suffix)
		for i in range(len(self.words)):
			if len(self.words[i]) >= prelen and len(self.words[i]) >= suflen:
				if self.words[i][0:prelen] == prefix and self.words[i][-suflen:] == suffix:
					index = i
		if index == -1:
			return -1
		else:
			return index

# Your WordFilter object will be instantiated and called as such:
words = ["apple"]
obj = WordFilter(words)
a = obj.f("a", "e")
print(a)