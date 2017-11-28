class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = n // 5
        return x + self.trailingZeroes(x) if x else 0