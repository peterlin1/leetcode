class Solution(object):

    def plusOne(self, digits):
        """
        Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
        The digits are stored such that the most significant digit is at the head of the list, and each element in the
        array contain a single digit.

        You may assume the integer does not contain any leading zero, except the number 0 itself.

        Runtime: 36 ms, faster than 86.40% of Python3 online submissions for Plus One.
        Memory Usage: 14 MB, less than 5.13% of Python3 online submissions for Plus One.


        Parameters
        ----------
        digits : list


        Returns
        -------
        ret : list


        Examples
        --------
        >>> Solution().plusOne([1,2,3])
        [1, 2, 4]

        >>> Solution().plusOne([1, 9, 9])
        [2, 0, 0]

        """

        n_digits = int(''.join(map(str, digits))) + 1
        return [int(x) for x in str(n_digits)]
