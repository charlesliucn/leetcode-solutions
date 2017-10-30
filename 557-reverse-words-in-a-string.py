class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = ""
        slist = s.split()
        for st in slist:
        	r += self.reverseWord(st)+" "
        r = r[:-1]
        return r

    
    def reverseWord(self, w):
    	s = ""
    	num = len(w)
    	for i in range(num):
    		s += w[num-i-1]
    	return s
