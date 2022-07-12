/* Peers
Brian Lucius
Yousuf Said
Tom Harris
Michael Stafford
Theo Shafer
*/

/* 
  Given a string,
  return a new string with the duplicates excluded
  Bonus: Keep only the last instance of each character.
*/

const str1 = "abcABC";
const expected1 = "abcABC";

const str2 = "helloo";
const expected2 = "helo";

const str3 = "";
const expected3 = "";

const str4 = "aa";
const expected4 = "a";

//bonus
const str5 = "aba"
const expected5 = "ba"

/**
 * De-dupes the given string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string that may contain duplicates.
 * @returns {string} The given string with any duplicate characters removed.
 */
function stringDedupe(str) {
    var lettersSet = new Set();
    var resultString = "";

    for (var i=str.length - 1; i>=0; i--) {
        lettersSet.add(str[i])
    }
    // console.log(lettersSet)

    for (var key of lettersSet) {
        resultString = key + resultString
    }
    return resultString
}



console.log(stringDedupe(str1));
console.log(stringDedupe(str2));
console.log(stringDedupe(str3));
console.log(stringDedupe(str4));
console.log(stringDedupe(str5));

// function stringDedupe(str) {
//     var new_string = "";
//     var freq = {};
//     for(i=0;i<str.length;i++){
//         let char = str[i];
//         if(freq[char]){
//             freq[char]++;
//         }
//         else {
//             freq[char] =1
//             new_string += char;
//         }
//     }
//     return new_string;
// }

// function stringDedupe(str = "") {
//     let distinctStr = "";
//     const seen = {};

//     // loop backwards to include last occurrence
//     for (let i = str.length - 1; i >= 0; --i) {
//         if (!seen[str[i]]) {
//             distinctStr = str[i] + distinctStr;
//             seen[str[i]] = true;
//         }
//     }
//     return distinctStr;
// }

/*****************************************************************************/

/* 
  Given a string containing space separated words
  Reverse each word in the string.
  If you need to, use .split to start, then try to do it without.
*/

const strA = "hello";
const expectedA = "olleh";

const strB = "hello world";
const expectedB = "olleh dlrow";

const strC = "abc def ghi";
const expectedC = "cba fed ihg";

/**
 * Reverses the letters in each words in the given space separated
 * string of words. Does NOT reverse the order of the words themselves.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str Contains space separated words.
 * @returns {string} The given string with each word's letters reversed.
 */
function reverseWords(str) {
    //Your code here
    var reversed = ""
    var curWord = ""
    for (var char of str) {
        if (char ==" ") {
            reversed+=curWord + " ";
            curWord = "";
        } else {
            curWord = char + curWord;
        }
    }
    return reversed + curWord
}

function reverseWordsSplit(wordsStr) {
    const words = wordsStr.split(" ");
    let wordsReversed = "";

    for (const word of words) {
        let reversedWord = "";

        for (let i = word.length - 1; i >= 0; --i) {
            reversedWord += word[i];
        }

        // add a space in front of word if it's not the first word
        if (wordsReversed.length > 0) {
            reversedWord = " " + reversedWord;
        }
        wordsReversed += reversedWord;
    }
    return wordsReversed;
}

console.log(reverseWords(strA)) //expectedA: olleh
console.log(reverseWords(strB)) //expectedB: olleh dlrow
console.log(reverseWords(strC)) //expectedC: cba fed ihg