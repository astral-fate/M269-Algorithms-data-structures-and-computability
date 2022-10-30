
def longestConsecutive(nums):
  arr = []
  for i in range(1, len(nums)):
      nums.sort()
      
      if nums[i] !=nums[i+1]:
          continue
      
      
      if nums[i] in range(1, nums[-1]):
          if nums[i]+1:
              arr.append(i)         
      else:
          break      
  return len(arr)
  
      
# Python3 program to find longest
# contiguous subsequence

# Returns length of the longest
# contiguous subsequence


nums = [0,3,7,2,5,8,4,6,0,1]
print(longestConsecutive(nums))
