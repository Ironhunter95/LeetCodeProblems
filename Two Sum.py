class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)==1:
            return [0]
        elif len(nums)==2:
            return [0,1]
        elif len(nums)>2:
            indexi=0
            indexj=1
            for i in nums:
                for j in nums[indexi+1:]:
                    if i+j == target:
                        return [indexi,indexj]
                    indexj+=1
                indexi+=1
                indexj=indexi+1