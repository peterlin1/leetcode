class Solution(object):

    def detectCapitalUse(self, word):
        """
        Given a word, you need to judge whether the usage of capitals in it is right or not.

        We define the usage of capitals in a word to be right when one of the following cases holds:

        All letters in this word are capitals, like "USA".
        All letters in this word are not capitals, like "leetcode".
        Only the first letter in this word is capital, like "Google".
        Otherwise, we define that this word doesn't use capitals in a right way.

        Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.

        Runtime: 32 ms, faster than 36.82% of Python3 online submissions for Detect Capital.
        Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Detect Capital.


        Parameters
        ----------
        word : str


        Returns
        -------

        ret : bool


        Examples
        --------
        >>> Solution().detectCapitalUse("FlaG")
        False

        >>> Solution().detectCapitalUse("USA")
        True

        """

        can_low = can_cap = True

        for idx in range(len(word)):
            if word[idx].isupper():
                if not can_cap:
                    return False

                if idx > 0 and can_cap:
                    can_low = False

            else:
                if not can_low:
                    return False

                can_cap = False
        return True
