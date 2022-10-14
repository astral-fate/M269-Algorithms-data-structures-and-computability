 """
 
 first shoot


 class Solution(object):
    def isValid(self, s):
       
        :type s: str
        :rtype: bool
        
        for i in range(len(s)):
          if i+i+1=="()" or "{}" or "[]":
            return bool(True)
      
          else:
            return bool(False)
            
     
     second shoot 
     
     class Solution(object):
    def isValid(self, s):

        for i in range(len(s)):
          if i+i+1=="()" or "{}" or "[]":
            return bool(True)
      
          elif i+i+1=="(}" or "{)" or "[}":
            return bool(False)
          else:
            return bool(False) 
     
     
      tip for improvement: how about using a data structure so we can access the index, more efficiently?
      so instead of i+i+1 how about s[i]+s[i+1]?. This is very specfic case in wich the input it only two chars, and we want to generlize it to more broader case
      
      refrenced solution 
      
      def isValid(s):
    stack = []
    for i in range(len(s)):
        if s[i] == "(" or s[i] == "{" or s[i] == "[":
            stack.append(i)
        elif len(stack) <= 0:
            return False
        else:
            l_idx=stack.pop()
            if s[i] == ")" and s[l_idx] != "(":
                return False
            elif s[i] == "]" and s[l_idx] != "[":
                return False
            elif s[i] == "}" and s[l_idx] != "{":
                return False
    if len(stack) == 0:
        return True
    return False
    
    https://leetcode.com/problems/valid-parentheses/discuss/603002/Python-3-simple-scanning-with-loop
      
      """ 
