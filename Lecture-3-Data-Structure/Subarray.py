"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

refrence 
https://leetcode.com/problems/subarray-sum-equals-k/

visulize 

https://pythontutor.com/render.html#mode=display

"""



def subarraySum(nums, k):
    ans, n = 0, len(nums)
    preSum = [nums[0]]
    dic = {}
    dic[0] = 1
    for i in nums[1:]:
        preSum.append(i+preSum[-1])
    for i in preSum:
        if i-k in dic:
            ans+=dic[i-k]
        dic[i] = dic.get(i,0) + 1 
    return ans
    


nums = [ 3,1, 8, 7]
k = 4
 
print(subarraySum(nums, k))
