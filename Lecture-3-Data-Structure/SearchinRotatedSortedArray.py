    

"""

class Solution:

    def search(self, nums, target):

    

        :type nums: List[int]

        :type target: int

        :rtype: int

        

        for i in range(len(nums)):

            if nums[i]==target:

                return i

        return -1

    

    

"""

class Solution(object):

    def search(self, nums, target):

        """

        :type nums: List[int]

        :type target: int

        :rtype: int

        """

        map = {}

        for i in range (0, len(nums)):

            map[nums[i]] = i

        

        if target in map:

            return map[target]

        else:

            return -1

        print(map)
