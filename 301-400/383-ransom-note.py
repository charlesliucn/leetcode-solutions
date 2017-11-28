class Solution(object):
	def canConstruct(self, ransomNote, magazine):
		"""
		:type ransomNote: str
		:type magazine: str
		:rtype: bool
		"""
		ransomNote = list(ransomNote)
		magazine = list(magazine)
		if len(ransomNote) == 0:
			return True
		try:
			for i in ransomNote:
				magazine.remove(i)
			return True
		except ValueError:
			return False