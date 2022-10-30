
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






def longestConsecutive(nums):
  arr = []
  j=0
  nums.sort()
  for i in range(0,len(nums)):
     
     
      
      if nums[i] == nums[i]+1:
          nums.pop(i)
          
      
      
      if nums[i] in range(0,nums[-1]):
          if nums[i]+1:
              arr.append(i)
              
              
      
  return len(arr)   
  
      
# Python3 program to find longest
# contiguous subsequence

# Returns length of the longest
# contiguous subsequence


nums = [0,3,7,2,5,8,4,6,0,1]
print(longestConsecutive(nums))



def longestConsecutive(nums):
  arr = []
  j=0
  nums.sort()
  for i in range(0,len(nums)):
      

      if nums[i] == nums[i]+1:
          nums.pop(i)
         for i in nums:
           if nums[i] in range(0,nums[-1]):
              if nums[i]+1 in nums:
                  arr.append(i)
              
              
      
  return len(arr)   
  
      
# Python3 program to find longest
# contiguous subsequence

# Returns length of the longest
# contiguous subsequence


nums = [0,13,17,12,15,18,14,16,10,11]
print(longestConsecutive(nums))
