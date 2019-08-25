class Solution(object):

    def lengthOfLastWord(self, s):
        """
        Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of
        last word in the string.

        If the last word does not exist, return 0.

        Note: A word is defined as a character sequence consists of non-space characters only.

        Runtime: 32 ms, faster than 89.99% of Python3 online submissions for Length of Last Word.
        Memory Usage: 13.9 MB, less than 5.26% of Python3 online submissions for Length of Last Word.


        Parameters
        ----------
        s : str


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().lengthOfLastWord("Hello World")
        5

        """

        if len(s) == 0:
            return 0

        s = s.strip()
        word = s.split(" ")[-1]
        return len(word)
