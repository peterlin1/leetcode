import re


class Solution(object):

    def backspaceCompare(self, S, T):
        """
        Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a
        backspace character.

        Note:
        1 <= S.length <= 200
        1 <= T.length <= 200
        S and T only contain lowercase letters and '#' characters.

        Follow up:
        Can you solve it in O(N) time and O(1) space?

        104 / 104 test cases passed.
        Status: Accepted
        Runtime: 36 ms
        Memory Usage: 13.9 MB


        Parameters
        ----------
        S : str
        T : str


        Returns
        -------
        ret : bool


        Examples
        --------
        >>> Solution().backspaceCompare(S="ab#c", T="ad#c")
        True

        >>> Solution().backspaceCompare(S="ab##", T="c#d#")
        True

        >>> Solution().backspaceCompare(S="a##c", T="#a#c")
        True

        >>> Solution().backspaceCompare(S="a#c", T="b")
        False

        """

        n_S = re.sub(r"""[a-z]#""", "", S).lstrip('#')
        n_T = re.sub(r"""[a-z]#""", "", T).lstrip('#')

        if n_S == n_T:
            return True
        if (n_S == S) and (n_T == T):
            return False
        return self.backspaceCompare(n_S, n_T)

