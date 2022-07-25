/* 
Recursive Sigma
Input: integer
Output: sum of integers from 1 to Input integer
*/

const num1 = 5;
const expected1 = 15;
// Explanation: (1+2+3+4+5)

const num2 = 2.5; 
const expected2 = 3;
// Explanation: (1+2)

const num3 = -1;
const expected3 = 0;

/**
 * Recursively sum the given int and every previous positive int.
 * - Time: O(?).
 * - Space: O(?).
 * @param {number} num
 * @returns {number}
 */

function recursiveSigma(num) {
    //Your code here
    //Sanitize value?
    //Base case?
    //Recursive call?
    var rounded = Math.floor(num)

    if(rounded <= 0) {
        return 0
    }
    return rounded + recursiveSigma(--rounded)
    // return rounded + recursiveSigma(rounded - 1)
}

console.log(recursiveSigma(num1)); // 15
console.log(recursiveSigma(num2)); // 3
console.log(recursiveSigma(num3)); // 0