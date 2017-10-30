class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        bits = []
        while True:
            if n == 0:
                break
            n, r = divmod(n, 2)
            bits.append(r)
        bitnum = len(bits)
        for i in range(bitnum-1):
        	if bits[i] == bits[i+1]:
        		return False
        return True