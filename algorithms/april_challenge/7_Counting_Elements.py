from collections import Counter


class Solution(object):

    def countElements(self, arr):
        """
        Given an integer array arr, count element x such that x + 1 is also in arr.

        If there're duplicates in arr, count them separately.

        Constraints:
        1 <= arr.length <= 1000
        0 <= arr[i] <= 1000

        35 / 35 test cases passed.
        Status: Accepted
        Runtime: 32 ms
        Memory Usage: 14.1 MB


        Parameters
        ----------
        arr : list


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().countElements([1, 2, 3])
        2

        >>> Solution().countElements([1, 1, 3, 3, 5, 5, 7, 7])
        0

        >>> Solution().countElements([1, 3, 2, 3, 5, 0])
        3

        >>> Solution().countElements([1, 1, 2, 2])
        2

        """

        c_arr = Counter(arr)
        ret = 0
        for val in c_arr:
            if c_arr[val + 1] > 0:
                ret += c_arr[val]
        return ret
