class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        newArr = []
        for i in range(len(nums-1)):
          for j in range(len(nums-i-1)):
            newArr = nums[i]+nums[i+1]
            
          if newArr == target:
        print([i],[i])
          
          
        
