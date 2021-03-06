class Solution(object):

    def findTheDifference(self, s, t):
        """
        Given two strings s and t which consist of only lowercase letters.

        String t is generated by random shuffling string s and then add one more letter at a random position.

        Find the letter that was added in t.

        Runtime: 40 ms, faster than 66.53% of Python3 online submissions for Find the Difference.
        Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Find the Difference.


        Parameters
        ----------
        s : str

        t : str


        Returns
        -------
        ret : str


        Examples
        --------
        >>> Solution().findTheDifference("abcd", "abcde")
        'e'

        """

        a_sum = 0
        for idx in range(len(s)):
            a_sum = a_sum ^ ord(s[idx]) ^ ord(t[idx])
        a_sum ^= ord(t[-1])
        return str(chr(a_sum))
