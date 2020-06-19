class Solution(object):

    def hIndex(self, citations):
        """
        Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher,
        write a function to compute the researcher's h-index.

        According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at
        least h citations each, and the other N − h papers have no more than h citations each."

        Note:
        If there are several possible values for h, the maximum one is taken as the h-index.

        Follow up:
        This is a follow up problem to H-Index, where citations is now guaranteed to be sorted in ascending order.
        Could you solve it in logarithmic time complexity?

        Runtime: 144 ms, faster than 90.63% of Python3 online submissions for H-Index II.
        Memory Usage: 20.5 MB, less than 16.32% of Python3 online submissions for H-Index II.


        Parameters
        ----------
        citations : list


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().hIndex([0, 1, 3, 5, 6])
        3

        """

        left = 0
        right = len(citations) - 1
        while left <= right:
            mid = left + ((right - left) // 2)
            if citations[mid] >= len(citations) - mid:
                right = mid - 1
            else:
                left = mid + 1
        return len(citations) - left
