class Solution(object):

    def countSegments(self, s):
        """
        Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space
        characters.

        Please note that the string does not contain any non-printable characters.

        Runtime: 28 ms, faster than 51.13% of Python3 online submissions for Number of Segments in a String.
        Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Number of Segments in a String.


        Parameters
        ----------
        s : str


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().countSegments("Hello, my name is John")
        5

        """

        return len(s.split())
