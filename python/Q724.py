class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 0 
        n = len(nums)
        for i in range(n):
            left = sum(nums[0:i+1])
            right = sum(nums[i:n])
            if left == right:
                return i
            else:
                left = 0
                right = 0
        
        if left ==0 and right ==0:
            return -1