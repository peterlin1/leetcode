class Solution(object):

    def reverseWords(self, s):
        """
        Given a string, you need to reverse the order of characters in each word within a sentence while still
        preserving whitespace and initial word order.

        Note: In the string, each word is separated by single space and there will not be any extra space in the string.

        Runtime: 32 ms, faster than 69.61% of Python3 online submissions for Reverse Words in a String III.
        Memory Usage: 13.3 MB, less than 96.15% of Python3 online submissions for Reverse Words in a String III.


        Parameters
        ----------
        s : str


        Returns
        -------
        ret : str


        Examples
        --------
        >>> Solution().reverseWords("Let's take LeetCode contest")
        "s'teL ekat edoCteeL tsetnoc"

        """

        ret = []
        for word in s.split(' '):
            ret.append(word[::-1])
        return ' '.join(ret)
