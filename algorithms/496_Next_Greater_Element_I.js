/**
 * You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find
 * all the next greater numbers for nums1's elements in the corresponding places of nums2.
 * The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not
 * exist, output -1 for this number.
 *
 * Note:
 * All elements in nums1 and nums2 are unique.
 * The length of both nums1 and nums2 would not exceed 1000.
 *
 * Runtime: 56 ms, faster than 96.31% of JavaScript online submissions for Next Greater Element I.
 * Memory Usage: 35.1 MB, less than 100.00% of JavaScript online submissions for Next Greater Element I.
 *
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var nextGreaterElement = function(nums1, nums2) {
    var ret = Array.apply(null, Array(nums1.length)).map(function () {return -1});

    for (var idx_1 = 0; idx_1 < nums1.length; idx_1++) {
        for (var idx = nums2.indexOf(nums1[idx_1]); idx < nums2.length; idx++) {
            if nums2[idx] > nums1[idx_1] {
                ret[idx_1] = nums2[idx];
                break;
            }
        }
    }
    return ret
};