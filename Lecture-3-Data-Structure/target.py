def solution(target):
    result = [target[0]] 
    # add the first element to the result array
    for i in range(1, len(target)-1):
        # iterate through the elements in the target array, starting from the second element
        if target[i] > max(target[i+1], target[i-1]): 
            # if the element is greater than its neighbors
            result.append(target[i]) # add it to the result array
            result.append(target[-1]) # add the last element to the result array
    return result
    
    
mylist =[1,3,2,6]

print(solution(mylist))


"""

The range function in Python generates a sequence of integers from a start value to an end value. By setting the start value to 1, we are starting the iteration at the second element of the target array. This is because we want to skip the first element, since it is already included in the result array.

Similarly, by setting the end value to len(target)-1, we are ending the iteration at the second to last element of the target array. This is because we want to skip the last element, since it is also already included in the result array.

By starting the iteration at the second element and ending it at the second to last element, we are able to iterate through all the elements of the target array except for the first and last elements. This allows us to check the elements in the middle of the array for the condition target[i] > max(target[i+1], target[i-1]).

The result array is initially initialized with the first and last elements of the target array, so we only need to check the elements in the middle of the array to see if they should be included in the result.


"""
