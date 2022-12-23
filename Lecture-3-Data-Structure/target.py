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