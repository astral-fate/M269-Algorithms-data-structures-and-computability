 """
# # # #  # #first shoot

class Solution(object):
    def twoSum(self, nums, target):
        
        newArr = []
        for i in range(len(nums-1)):
          for j in range(len(nums-i-1)):
            newArr = nums[i]+nums[i+1]
            
          if newArr == target:
        print([i],[i])
          
  ######second shoot

        newArr = []

        for a in range(len(nums)):
            for b in range(len(nums)):        

                newArr = a+b

            if newArr == target:
                return a,b
      
  

######second shoot


def twoSum(nums, target):

    newArr = []
    
    for i in range(len(nums)):
      for j in range(len(nums-i)):
          newArr = nums[a]+nums[b]
          
          if newArr == target:
              return nums[a]+nums[b]
        
nums = [2,7,11,15]      
print(twoSum(nums, 9))


######last and final shoot 


lesson learned:

practice on range syntax
practice more on len(nums), len(num-1), (len(nums-i-1)), etc

practice on return funcs
 """ 

class Solution(object):
    def twoSum(self, nums, target):
   
        newArr = []

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
              newArr = nums[i]+nums[j]

              if newArr == target:
                  return [i,j]
        

    

          
        
