class Solution(object):

    def canConstruct(self, ransomNote, magazine):
        """
        Given an arbitrary ransom note string and another string containing letters from all the magazines, write a
        function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will
        return false.

        Each letter in the magazine string can only be used once in your ransom note.

        Note:
        You may assume that both strings contain only lowercase letters.

        Runtime: 36 ms, faster than 96.59% of Python3 online submissions for Ransom Note.
        Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Ransom Note.


        Parameters
        ----------
        ransomNote : str

        magazine : str


        Returns
        -------
        ret : bool


        Examples
        --------
        >>> Solution().canConstruct("a", "b")
        False

        >>> Solution().canConstruct("aa", "aab")
        False

        """

        for idx in range(len(ransomNote)):
            try:
                f_idx = magazine.index(ransomNote[idx])
            except ValueError:
                return False
            magazine = magazine[0: f_idx] + magazine[f_idx + 1:]
            # print(ransomNote[idx], magazine)
        return True
