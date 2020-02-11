/**
 * Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American
 * keyboard like the image below.
 *
 * Note:
 *
 * You may use one character in the keyboard more than once.
 * You may assume the input string will only contain letters of alphabet.
 *
 * Runtime: 52 ms, faster than 71.99% of JavaScript online submissions for Keyboard Row.
 * Memory Usage: 33.8 MB, less than 50.00% of JavaScript online submissions for Keyboard Row.
 *
 * @param {string[]} words
 * @return {string[]}
 */
var mem = [2, 3, 3, 2, 1, 2, 2, 2, 1, 2, 2, 2, 3, 3, 1, 1, 1, 1, 2, 1, 1, 3, 1, 3, 1, 3];

var findWords = function(words) {
    ret = []
    for (var idx = 0; idx < words.length; idx++) {
        if (_is_same_row(words[idx]) == true) {
            ret.push(words[idx]);
        }
    }
    return ret;
};

function _is_same_row (word) {
    var row = -1;
    var u_word = word.toUpperCase();
    for (var idx = 0; idx < u_word.length; idx++) {
        if (row == -1) {
            row = mem[u_word.charCodeAt(idx) - 65];
            continue;
        }
        if (mem[u_word.charCodeAt(idx) - 65] != row) {
            return false;
        }
    }
    return true;
}