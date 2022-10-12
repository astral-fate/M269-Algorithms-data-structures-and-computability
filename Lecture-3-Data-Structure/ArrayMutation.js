/*
Given an array RealArr , your task is to apply the following mutation to it:
•	Array RealArr mutates into a new array NewArr of the same length
•	For each i from 0 to RealArr.length - 1 inclusive, 
•	NewArr[i] = RealArr  [i – 1 meaning (0 - (1)] + RealArr  [i] + RealArr  [i + 1]
Since im in the 0 index, and there's no index be4 me, hence …


 
•	If some element in the sum a[i - 1] + a[i] + a[i + 1] does not exist, it is considered to be 0
o	For example, b[0] equals 0 + a[0] + a[1]
Since we iterarte over len(i-1), we can't have index (-1), since the len(i-1), is already -1
Example
For a = [4, 0, 1, -2, 3], the output should be solution(a) = [4, 5, -1, 2, 1].
Explanation:
•	b[0] = 0 + a[0] + a[1] = 0 + 4 + 0 = 4
•	b[1] = a[0] + a[1] + a[2] = 4 + 0 + 1 = 5
•	b[2] = a[1] + a[2] + a[3] = 0 + 1 + (-2) = -1
•	b[3] = a[2] + a[3] + a[4] = 1 + (-2) + 3 = 2
•	b[4] = a[3] + a[4] + 0 = (-2) + 3 + 0 = 1
So, the mutated answer array is [4, 5, -1, 2, 1].
Input/Output
•	[execution time limit] 4 seconds (py)
•	[input] array.integer a
An array of integers that needs to be mutated.
Guaranteed constraints:
1 ≤ a.length ≤ 1000,
-103 ≤ a[i] ≤ 103.
•	[output] array.integer
The resulting array after the mutation.

refrence

https://stackoverflow.com/questions/71301895/codesignal-mutate-array

*/


function mutateTheArray(n, a) {
    let b = [];

    for (let i=0; i <= n-1; i++) {
        if (i==0) {
            b[0] = a[0] + a[1];
        } else if (i == n-1) { // <- here
            b[i] = a[i-1] + a[i];
        } else {
            b[i] = a[i-1] + a[i] + a[i+1];
        }
    }
    return b;
}
console.log(mutateTheArray(5, [4, 0, 1, -2, 3]));

