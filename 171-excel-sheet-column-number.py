class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = len(s)
        weight = 26**(num-1)
        sum_all = 0
        for i in range(num):
            bit = ord(s[i]) - ord('A') + 1
            sum_all += bit*weight
            weight = weight//26
        return sum_all