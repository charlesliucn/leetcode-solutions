class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        define_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}  
        num = 0  
        for i in range(len(s)):  
            if i == 0 or define_dict[s[i]] <= define_dict[s[i-1]]:  
                num += define_dict[s[i]]  
            else:  
                num += define_dict[s[i]] - 2*define_dict[s[i-1]]  
        return num