class Solution(object):

    def sortColors(self, nums):
        """
        Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color
        are adjacent, with the colors in the order red, white and blue.

        Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

        Follow up:
        A rather straight forward solution is a two-pass algorithm using counting sort.
        First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's,
        then 1's and followed by 2's.

        Could you come up with a one-pass algorithm using only constant space?


        Parameters
        ----------
        nums : list


        Examples
        --------
        >>> Solution().sortColors([2, 0, 2, 1, 1, 0])
        [0, 0, 1, 1, 2, 2]

        """

        # Solution submitted before edited note to discount built-in sort 
        nums.sort()
