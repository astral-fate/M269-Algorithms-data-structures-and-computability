"""

Codewriting
Given an array of positive integers a, your task is to calculate the sum of every possible a[i] ∘ a[j], where a[i] ∘ a[j] is the concatenation of the string representations of a[i] and a[j] respectively.
Example
•	For a = [10, 2], the output should be solution(a) = 1344.
o	a[0] ∘ a[0] = 10 ∘ 10 = 1010,
o	a[0] ∘ a[1] = 10 ∘ 2 = 102,
o	a[1] ∘ a[0] = 2 ∘ 10 = 210,
o	a[1] ∘ a[1] = 2 ∘ 2 = 22.
So the sum is equal to 1010 + 102 + 210 + 22 = 1344.
•	For a = [8], the output should be solution(a) = 88.
There is only one number in a, and a[0] ∘ a[0] = 8 ∘ 8 = 88, so the answer is 88.
•	For a = [1, 2, 3], the output should be solution(a) = 198.
o	a[0] ∘ a[0] = 1 ∘ 1 = 11,
o	a[0] ∘ a[1] = 1 ∘ 2 = 12,
o	a[0] ∘ a[2] = 1 ∘ 3 = 13,
o	a[1] ∘ a[0] = 2 ∘ 1 = 21,
o	a[1] ∘ a[1] = 2 ∘ 2 = 22,
o	a[1] ∘ a[2] = 2 ∘ 3 = 23,
o	a[2] ∘ a[0] = 3 ∘ 1 = 31,
o	a[2] ∘ a[1] = 3 ∘ 2 = 32,
o	a[2] ∘ a[2] = 3 ∘ 3 = 33.
The total result is 11 + 12 + 13 + 21 + 22 + 23 + 31 + 32 + 33 = 198.
Input/Output
•	[execution time limit] 4 seconds (py)
•	[input] array.integer a
A non-empty array of positive integers.
Guaranteed constraints:
1 ≤ a.length ≤ 105,
1 ≤ a[i] ≤ 106.
•	[output] integer64
The sum of all a[i] ∘ a[j]s. It's guaranteed that the answer is less than 253.
[Python 2] Syntax Tips

You are given two arrays of integers a and b of the same length, and an integer k. We will be iterating through array a from left to right, and simultaneously through array b from right to left, and looking at pairs (x, y), where x is from a and y is from b. Such a pair is called tiny if the concatenation xy is strictly less than k.
Your task is to return the number of tiny pairs that you'll encounter during the simultaneous iteration through a and b.

"""



def solution(a):
    sum = 0
    current_index_looking_at = 0
    for i in a:
        for x in a:
            temp = str(i)+str(x)
            sum += int(temp)
    return sum
