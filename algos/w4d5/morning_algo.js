/* 
  String Anagrams
  Given a string,
  return array where each element is a string representing a different anagram (a different sequence of the letters in that string).
  Ok to use built in methods
*/

const str1 = "lim";
const expected1 = ["ilm", "iml", "lim", "lmi", "mil", "mli"];


// const expected1 = ["ilm", "iml", "lim", "lmi", "mil", "mli"];
// Order of the output array does not matter

/**
 * Add params if needed for recursion.
 * Generates all anagrams of the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {Array<string>} All anagrams of the given str.
 */

function generateAnagrams2(str) { //don't be afraid to add parameters!
    //Your code here
    if (str.length <= 2) return str.length === 2 ? [str, str[1] + str[0]] : [str];
    return str
        .split('')
        .reduce(
            (acc, letter, i) =>
            acc.concat(generateAnagrams2(str.slice(0, i) + str.slice(i + 1)).map(val => letter + val)),
            []
        );
}

// function generateAnagrams3(str) {
//     if (str.length === 0) return "";
//     if (str.length === 1) return str;
    
//     let result = [];
    
//     for (let i=0; i<str.length; i++) {
//         const currentChar = str[i];
//         const remainingChars = str.slice() + str.slice();

//     }
// }

function generateAnagrams(str, anagrams=[], partial='') {
    if (!str) anagrams.push(partial);

    for (let i=0; i < str.length; i++) {
        const currentLetter = str[i];
        const restOfString = str.slice(0, i) + str.slice(i+1);
        const newPartial = partial + currentLetter;
        generateAnagrams(restOfString, anagrams, newPartial);
    }
    return anagrams;
}

// console.log(generateAnagrams(str1)) //["ilm", "iml", "lim", "lmi", "mil", "mli"] (order may vary, that's okay)
const str2 = "abcdefghijkl";
console.log(generateAnagrams(str2))


// a                0.048
// ab               0.052
// abc              0.052
// abcd             0.048
// abcde            0.051
// abcdef           0.049 
// abcdefg          0.051
// abcdefgh         0.058
// abcdefghi        0.094
// abcdefghij       0.473
// abcdefghijk      5.247
// abcdefghijkl     overflow
//