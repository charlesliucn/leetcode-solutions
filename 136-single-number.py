class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum1 = sum(nums)
        singlelist = list(set(nums))
        sum2 = 2*sum(singlelist)
        return sum2 - sum1