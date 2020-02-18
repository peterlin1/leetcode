class Solution(object):

    def distributeCandies(self, candies):
        """
        Given an integer array with even length, where different numbers in this array represent different kinds of
        candies. Each number means one candy of the corresponding kind. You need to distribute these candies equally in
        number to brother and sister. Return the maximum number of kinds of candies the sister could gain.

        Note:
        The length of the given array is in range [2, 10,000], and will be even.
        The number in given array is in range [-100,000, 100,000].

        Runtime: 896 ms, faster than 59.12% of Python3 online submissions for Distribute Candies.
        Memory Usage: 14.6 MB, less than 91.67% of Python3 online submissions for Distribute Candies.


        Parameters
        ----------
        candies : list


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().distributeCandies([1, 1, 2, 2, 3, 3])
        3

        >>> Solution().distributeCandies([1, 1, 2, 3])
        2

        """

        u_candies = len(set(candies))
        a_candies = len(candies) // 2
        if u_candies > a_candies:
            return a_candies
        return u_candies
