class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        bits = []
        while True:
            if num == 0:
                break
            num, r = divmod(num, 2)
            bits.append(r)

        bits_reverse = [ 1 - i for i in bits]
        blen = len(bits_reverse)
        x_reverse = 0
        for i in range(blen):
            x_reverse = x_reverse + bits_reverse[i]*(2**i)
       	return x_reverse