// /* 
//   Given a SORTED array of integers, dedupe the array 
//   Because array elements are already in order, all duplicate values will be grouped together.
//   Ok to use a new array
//   Bonus: do it in O(n) time (no nested loops, new array ok)
//   Bonus: Do it in-place (no new array)
//   Bonus: Do it in-place in O(n) time and no new array
//   Bonus: Keep it O(n) time even if it is not sorted
// */

// const nums1 = [1, 1, 1, 1];
// const expected1 = [1];

// const nums2 = [1, 1, 2, 2, 3, 3];
// const expected2 = [1, 2, 3];

// const nums3 = [1, 1, 2, 3, 3, 4];
// const expected3 = [1, 2, 3, 4];

// const nums4 = [1, 1];
// const expected4 = [1];

// const nums5 = [9, 9, 9, 8, 8, 6, 6, 6, 2, 2, 1];
// const expected5 = [9, 8, 6, 2, 1];

// /**
//  * De-dupes the given sorted array.
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {Array<number>} nums
//  * @returns {Array<number>} The given array deduped.
//  */
// function dedupeSorted(nums) {
//   var x = 0;
//   while ( x < nums.length) {
//     if (nums[x] == nums[x+1]) {
//       nums.splice(x+1,1);
//     } else x++;
//   }
//   return nums;
// }

// console.log("Expected: ", expected1, "\nReturned: ", dedupeSorted(nums1), "\n");
// console.log("Expected: ", expected2, "\nReturned: ", dedupeSorted(nums2), "\n");
// console.log("Expected: ", expected3, "\nReturned: ", dedupeSorted(nums3), "\n");
// console.log("Expected: ", expected4, "\nReturned: ", dedupeSorted(nums4), "\n");
// console.log("Expected: ", expected5, "\nReturned: ", dedupeSorted(nums5), "\n");


/*****************************************************************************/


/* 
  Given an array of integers
  return the first integer from the array that is not repeated anywhere else
  If there are multiple non-repeated integers in the array,
  the "first" one will be the one with the lowest index.
*/

const twoNums1 = [3, 5, 4, 3, 4, 6, 5];
const twoExpected1 = 6;

const twoNums2 = [3, 5, 5];
const twoExpected2 = 3;

const twoNums3 = [3, 3, 5];
const twoExpected3 = 5;

const twoNums4 = [5];
const twoExpected4 = 5;

const twoNums5 = [];
const twoExpected5 = null;

/**
 * Finds the first int from the given array that has no duplicates. I.e., the
 *    item at the lowest index that doesn't appear again in the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number|null} The first int value from the given array that has no
 *    dupes or null if there is none.
 */
 function firstNonRepeated(nums) {
  let numObject = {};
  let allLowestIndex = nums.length;
  let lowestNoDupes = 0;

  for(var i = nums.length-1; i >= 0; i--){
      if(!(nums[i] in numObject)){
          numObject[nums[i]] = { times: 1, lowestIndex: i};
      }
      else{
          numObject[nums[i]].times++;
          numObject[nums[i]].lowestIndex = i;
      }
  }
  let isFound = false;

  for(key in numObject){
      number = numObject[key];
      if(number.times == 1 && number.lowestIndex < allLowestIndex){
          allLowestIndex = number.lowestIndex;
          lowestNoDupes = +key;
          isFound = true;
      }
  }
  if(isFound == false){
      return null
  }

  return lowestNoDupes
}
function firstNonRepeated2(nums) {

const freq = {};

for (const num of nums) {
  if (freq.hasOwnProperty(num)) {
    freq[num]++;
  } else {
    freq[num] = 1
  }
}

for (const num of nums) {
  if (freq[num] === 1) {
    return num;
  }
}

return null
}

console.log("Expected: ", twoExpected1, "\nReturned: ", firstNonRepeated(twoNums1), "\n");
console.log("Expected: ", twoExpected2, "\nReturned: ", firstNonRepeated(twoNums2), "\n");
console.log("Expected: ", twoExpected3, "\nReturned: ", firstNonRepeated(twoNums3), "\n");
console.log("Expected: ", twoExpected4, "\nReturned: ", firstNonRepeated(twoNums4), "\n");
console.log("Expected: ", twoExpected5, "\nReturned: ", firstNonRepeated(twoNums5), "\n");

console.log("Expected: ", twoExpected1, "\nReturned: ", firstNonRepeated2(twoNums1), "\n");
console.log("Expected: ", twoExpected2, "\nReturned: ", firstNonRepeated2(twoNums2), "\n");
console.log("Expected: ", twoExpected3, "\nReturned: ", firstNonRepeated2(twoNums3), "\n");
console.log("Expected: ", twoExpected4, "\nReturned: ", firstNonRepeated2(twoNums4), "\n");
console.log("Expected: ", twoExpected5, "\nReturned: ", firstNonRepeated2(twoNums5), "\n");