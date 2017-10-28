class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1 if x > 0 else -1
        x = abs(x)
        bits = []
        while True:
            if x == 0:
                break
            x, r = divmod(x, 10)
            bits.append(r)
        num = len(bits)
        x_reverse = 0
        for i in range(num):
            x_reverse = x_reverse + bits[i]*(10**(num-i-1))
        if x_reverse >= 2**31 :
            return 0
        else:
            return x_reverse*flag