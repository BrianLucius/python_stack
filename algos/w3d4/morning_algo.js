// /* 
//   Given an int to represent how much change is needed
//   calculate the fewest number of coins needed to create that change,
//   using the standard US denominations
// */

// const cents1 = 25;
// const expected1 = "{ quarter: 1 }";

// const cents2 = 50;
// const expected2 = "{ quarter: 2 }";

// const cents3 = 9;
// const expected3 = "{ nickel: 1, penny: 4 }";

// const cents4 = 99;
// const expected4 = "{ quarter: 3, dime: 2, penny: 4 }";

// /**
//  * Calculates the fewest coins of the standard American denominations needed
//  *    to reach the given cents amount.
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {number} cents
//  * @param {string} sick
//  * @returns {Object<string, number>} - A denomination table where the keys are
//  *    denomination names and the value is the amount of that denomination
//  *    needed.
//  */
// function fewestCoinChange(cents) {
//     var change = {
//         'penny': 0,
//         'nickle' : 0,
//         'dime' : 0,
//         'quarter' : 0
//     };
//     change['quarter'] = 1;
//     console.log(change)
// }

// console.log("Expected: ", expected1, "\nReturned: ", fewestCoinChange(cents1), "\n");
// console.log("Expected: ", expected2, "\nReturned: ", fewestCoinChange(cents2), "\n");
// console.log("Expected: ", expected3, "\nReturned: ", fewestCoinChange(cents3), "\n");
// console.log("Expected: ", expected4, "\nReturned: ", fewestCoinChange(cents4), "\n");

/* 
  Missing Value
  You are given an array of length N that contains, in no particular order,
  integers from 0 to N . One integer value is missing.
  Quickly determine and return the missing value.
*/

const twoNums1 = [3, 0, 1];
const twoExpected1 = 2;

const twoNums2 = [3, 0, 1, 2];
const twoExpected2 = null;
// Explanation: nothing is missing

/* 
  Bonus: now the lowest value can now be any integer (including negatives),
  instead of always being 0. 
*/

const twoNums3 = [2, -4, 0, -3, -2, 1];
const twoExpected3 = -1;

const twoNums4 = [5, 2, 7, 8, 4, 9, 3];
const twoExpected4 = 6;

/**
 * Determines what the missing int is in the given unordered array of ints
 *    which spans from 0 to N where only one int is missing. With this missing
 *    int, a consecutive sequence of ints could be formed from the array.
 * Bonus: Given ints can span from N to M (start and end anywhere).
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} unorderedNums
 * @returns {number|null} The missing integer needed to be able to form an unbroken
 *    consecutive set of integers from the given array or null if none is missing.
 */
function missingValue(unorderedNums) {

    // var lowestNum = unorderedNums[0];
    // var highestNum = unorderedNums[0];

    // for (var i = 0; i < unorderedNums.length; i++) {
    //     if (unorderedNums[i] > highestNum) {
    //         highestNum = unorderedNums[i];
    //     }
    //     if (unorderedNums[i] < lowestNum) {
    //         lowestNum = unorderedNums[i];
    //     }
        
    // }

    var lowestNum = Math.min(...unorderedNums);
    var highestNum = Math.max(...unorderedNums);

    for (var i = lowestNum; i <= highestNum; i++) {
        if (!unorderedNums.includes(i)) {
            return i;
        }
    }

    return null

}

console.log("Expected: ", twoExpected1, "\nReturned: ", missingValue(twoNums1), "\n");
console.log("Expected: ", twoExpected2, "\nReturned: ", missingValue(twoNums2), "\n");
console.log("Expected: ", twoExpected3, "\nReturned: ", missingValue(twoNums3), "\n");
console.log("Expected: ", twoExpected4, "\nReturned: ", missingValue(twoNums4), "\n");

