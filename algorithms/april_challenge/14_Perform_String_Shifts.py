class Solution(object):

    def stringShift(self, s, shift):
        """
        You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction,
        amount]:

        direction can be 0 (for left shift) or 1 (for right shift).
        amount is the amount by which string s is to be shifted.
        A left shift by 1 means remove the first character of s and append it to the end.
        Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
        Return the final string after all operations.

        Constraints:
        1 <= s.length <= 100
        s only contains lower case English letters.
        1 <= shift.length <= 100
        shift[i].length == 2
        0 <= shift[i][0] <= 1
        0 <= shift[i][1] <= 100

        31 / 31 test cases passed.
        Status: Accepted
        Runtime: 36 ms
        Memory Usage: 13.9 MB


        Parameters
        ----------
        s : str

        shift : list


        Returns
        -------
        ret : str


        Examples
        --------
        >>> Solution().stringShift(s="abc", shift=[[0, 1], [1, 2]])
        "cab"

        >>> Solution().stringShift(s="abcdefg", shift=[[1, 1], [1, 1], [0, 2], [1, 3]])
        "efgabcd"

        """

        t_s = 0
        for sh in shift:
            if sh[0] is 0:
                t_s -= sh[1]
            else:
                t_s += sh[1]

        t_s %= len(s)
        return s[len(s) - t_s:] + s[: len(s) - t_s] if t_s >= 0 else s[-t_s:] + s[: -t_s]
