class Solution(object):

    def findWords(self, words):
        """
        Given a List of words, return the words that can be typed using letters of alphabet on only one row's of
        American keyboard like the image below.

        Note:
        You may use one character in the keyboard more than once.
        You may assume the input string will only contain letters of alphabet.

        Runtime: 20 ms, faster than 97.07% of Python3 online submissions for Keyboard Row.
        Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Keyboard Row.


        Parameters
        ----------
        words : list


        Returns
        -------
        ret : list


        Examples
        --------
        >>> Solution().findWords(["Hello", "Alaska", "Dad", "Peace"])
        ["Alaska", "Dad"]

        """

        def _is_same_row(word):
            row = None
            for char in word:
                # print(f"{word}, {char.upper()}")
                if not row:
                    row = mem[ord(char.upper()) - 65]
                    continue
                if mem[ord(char.upper()) - 65] != row:
                    return False
            return True

        # ASCII dec values of A - Z: 65 - 90
        mem = [2, 3, 3, 2, 1, 2, 2, 2, 1, 2, 2, 2, 3, 3, 1, 1, 1, 1, 2, 1, 1, 3, 1, 3, 1, 3]
        ret = []
        for word in words:
            if _is_same_row(word):
                ret.append(word)
        return ret
