class Solution(object):

    def reverseVowels(self, s):
        """
        Write a function that takes a string as input and reverse only the vowels of a string.

        The vowels does not include the letter "y".

        Runtime: 52 ms, faster than 87.56% of Python3 online submissions for Reverse Vowels of a String.
        Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Reverse Vowels of a String.


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
        ret = list(s)

        for idx in range(len(s)):
            if s[idx] in vowels:
                ret[idx] = next(rest)

        return "".join(ret)
