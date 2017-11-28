class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        import itertools
        slist = list(s)
        num_times = [len(list(v)) for k, v in itertools.groupby(slist)]
        numlen = len(num_times)
        totaltime = 0
        for i in range(numlen-1):
        	totaltime += min(num_times[i],num_times[i+1])
        return totaltime
