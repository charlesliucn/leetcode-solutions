class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        rstack = []
        for i in ops:
            if self.is_number(i):
                rstack.append(int(i))
                print(rstack)
            elif i == "D":
                rstack.append(rstack[-1]*2)
            elif i == "+":
                rstack.append(rstack[-1] + rstack[-2])
            elif i == "C":
                rstack.pop()
        sum_all = 0
        for i in rstack:
            sum_all += i
        return sum_all

    def is_number(self,s):
        try:
            float(s)
            return True
        except ValueError:
            pass
        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass
        return False