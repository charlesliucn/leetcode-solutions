class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for i in nums2:
        	if i in nums1:
        		nums1.remove(i)
        		res.append(i)
        return res