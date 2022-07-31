/*
  Recursive Binary Search
  Input: SORTED array of ints, int value
  Output: bool representing if value is found
  Recursively search to find if the value exists, do not loop over every element.
  Approach:
  Take the middle item and compare it to the given value.
  Based on that comparison, narrow your search to a particular section of the array
*/

const nums1 = [1, 3, 5, 6];
const searchNum1 = 4;
const expected1 = false;

const nums2 = [4, 5, 6, 8, 12];
const searchNum2 = 5;
const expected2 = true;

const nums3 = [3, 4, 6, 8, 12];
const searchNum3 = 3;
const expected3 = true;

/**
 * Add params if needed for recursion
 * Recursively performs a binary search (divide and conquer) to determine if
 * the given sorted nums array contains the given number to search for.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} sortedNums
 * @param {number} searchNum
 * @returns {boolean} Whether the searchNum was found in the sortedNums array.
 */
function binarySearch(sortedNums, searchNum, leftIndex= 0, rightIndex = sortedNums.length -1) { //will we need more parameters?
    //Your code here
    //Base case
    //primary logic
    //recursive call(s)
    console.log("left index:", leftIndex, "rightindex :", rightIndex)
    let middleIndex = parseInt((rightIndex - leftIndex) / 2)
    console.log(middleIndex)
    if(sortedNums[middleIndex] == searchNum){
        return true
    }
    else if(leftIndex == rightIndex){
        return false
    }
    else if(sortedNums[middleIndex] < searchNum){
        return binarySearch(sortedNums,searchNum,leftIndex, middleIndex)
    }
    else if(sortedNums[middleIndex] > searchNum){
        return binarySearch(sortedNums,searchNum,middleIndex, rightIndex)
    }
    return false
}

function binarySearch_spencer(sortedNums, searchNum, left=0, right=sortedNums.length-1) {
    if (left > right) {
        return false;
    }
    const mid = Math.floor((left + right) / 2);
    if (sortedNums[mid] === searchNum) {
        return true;
    }
    if (sortedNums[mid] > searchNum) {
        return binarySearch(sortedNums, searchNum, left, mid - 1);
    }
    return binarySearch(sortedNums, searchNum, mid + 1, right);
}

console.log(binarySearch(nums1, searchNum1)); // false
console.log(binarySearch(nums2, searchNum2)); // true
console.log(binarySearch(nums3, searchNum3)); // true