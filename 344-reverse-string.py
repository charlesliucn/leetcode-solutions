class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = ""
        num = len(s)
        for i in range(num):
        	r = r + s[num-1-i]
        return r