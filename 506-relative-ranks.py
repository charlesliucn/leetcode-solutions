class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        import numpy as np
        nums = np.array(nums)
        indices = np.argsort(nums)
        indices = indices[::-1]
        strs = ["Gold Medal", "Silver Medal","Bronze Medal"]
        for i in range(4, len(nums)+1):
        	strs.append(str(i))
        strs_ret = [""]*len(nums)
        for i in range(len(nums)):
        	strs_ret[indices[i]] = strs[i]
        return strs_ret

if __name__ == '__main__':
	t = Solution()
	print(t.findRelativeRanks([1]))