class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        len1 = len(nums)
        len2 = len(set(nums))
        if len1 > len2:
        	return True
        else:
        	return False