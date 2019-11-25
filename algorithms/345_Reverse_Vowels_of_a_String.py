class Solution(object):

    def reverseVowels(self, s):
        """
        Write a function that takes a string as input and reverse only the vowels of a string.

        The vowels does not include the letter "y".

        Runtime: 48 ms, faster than 93.80% of Python3 online submissions for Reverse Vowels of a String.
        Memory Usage: 14 MB, less than 93.33% of Python3 online submissions for Reverse Vowels of a String.


        Parameters
        ----------
        s : str


        Returns
        -------
        ret : str


        Examples
        --------
        >>> Solution().reverseVowels("leetcode")
        "leotcede"

        >>> Solution().reverseVowels("Aa")
        "aA"

        """

        vowels = set("aeiouAEIOU")
        rest = (val for val in s[:: -1] if val in vowels)
        ret = [next(rest) if val in vowels else val for val in s]

        return "".join(ret)

