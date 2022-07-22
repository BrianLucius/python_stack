/* 
  Array: Mode
  
  Create a function that, given an array of ints,
  returns the int that occurs most frequently in the array.
  What if there are multiple items that occur the same number of time?
    - return all of them (in an array)
    - what if all items occur the same number of times?
      - return empty array
*/

const nums1 = [];
const expected1 = [];

const nums2 = [1];
const expected2 = [1];

const nums3 = [5, 1, 4];
const expected3 = [];

const nums4 = [5, 1, 4, 1];
const expected4 = [1];

const nums5 = [5, 1, 4, 1, 5];
const expected5 = [5, 1]; // or [1,5]
//  - order doesn't matter

/**
 * Finds the mode or all modes if there are more than one. The mode is the
 *    value which occurs the most times in the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums Test
 * @returns {Array<number>} Mode or modes in any order.
 */

 function mode_spencer(nums) {
    if (nums.length === 1 || nums.length === 0) {
        return nums;
    }
  
    let modes = [];
    let maxCount = 0;
    let allSame = true;
    let freqs = {}
  
    for (let num of nums){
        freqs[num] = freqs[num] + 1 || 1 ; //builds freq table
        maxCount = Math.max(maxCount, freqs[num]);
    }
    let keycount = 0
    for (let key in freqs){
        keycount++
        if (freqs[key] === maxCount){
            modes.push(parseInt(key));
        }else{
            allSame = false;
        }
    }
    if (keycount == 1) return [nums[0]]
    return allSame ? [] : modes;
  
  }

function makeFrequencyTable(arr) {
    var frequency ={};

    for (i = 0; i < arr.length; i++) {
        // if given index of array is equal to an index in dict
        // if not there, add current array item in dictionary
        if (frequency.hasOwnProperty(arr[i])) {
            frequency[arr[i]] = frequency[arr[i]] + 1;
        } else {
            frequency[arr[i]] = 1;
        }
    }
    return frequency;
}

function mode(nums) {
    // var 
    // var 
    // for (var i=0; i<= ; i++) {

    // }
    var histogram = makeFrequencyTable(nums);
    console.log("histogram:", histogram);

    const values = Object.values(histogram);
    console.log("obj values:", values); 

    const maxFreq = Math.max(...values);
    console.log("max value:", maxFreq);
    // return makeFrequencyTable(nums);

    var modes = [];
    for (var [key, val] of histogram) {
        console.log(key, val);
        if (val == maxFreq) {
            modes+=maxFreq;
        }
    }
    return modes;

    // return histogram.keys() = max;

}

// console.log(mode(nums1)) // []
// console.log(mode(nums2)) // [1]
// console.log(mode(nums3)) // []
// console.log(mode(nums4)) // [1]
console.log(mode(nums5)) // [5, 1]



// // Caleb's implementation:
// function mode(nums) {
//     // if only one number is in starting array, return that array as it is the mode
//     if (nums.length === 1){
//         return nums;
//     }
    
//     let numDict = countNumberFrequency(nums);
//     console.log(numDict);
//     let maxFreq = 2;
//     let newArray = [];
    
//     for (let [key, val] of Object.entries(numDict)){
//         // console.log("key: "+key+" value: "+val);
//         if (val == maxFreq){
//             newArray.push(key);
//         } else if (val > maxFreq) {
//             newArray = [key];
//             maxFreq = val;
//         }
//     }
    
//     // if length of the new array is == to the length of the dictionary, 
//     // we know that all numbers are same frequency therefore return an empty array
//     if( Object.keys(numDict).length === newArray.length ){ //wrong need to fix this....
//         return ["test"];
//     }

//     return newArray;

// }

// function countNumberFrequency(arr) {
//     // returns a dictionary with { key (number): val (count) } given an array of numbers
//     let frequencyCount = {};
//     for ( let i = 0; i < arr.length; i++){
//         if(frequencyCount[arr[i]]){
//             frequencyCount[arr[i]]++;
//         }else{
//             frequencyCount[arr[i]] = 1;
//         }
//     }
//     return frequencyCount;
// }