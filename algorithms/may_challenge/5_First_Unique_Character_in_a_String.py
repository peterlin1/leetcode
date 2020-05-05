class Solution(object):

    def firstUniqChar(self, s):
        """
        Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return
        -1.

        104 / 104 test cases passed.
        Status: Accepted
        Runtime: 104 ms
        Memory Usage: 14.2 MB


        Parameters
        ----------
        s : str


        Returns
        -------
        ret: int

        """

        # right-most occurrence of char at index
        seq = [-1] * len(s)
        seen = set()
        for idx in range(len(s) - 1, -1, -1):
            if s[idx] in seen:
                seq[idx] = -1
            else:
                seq[idx] = idx
                seen.add(s[idx])

        # left-most occurrence of char at index
        # r_seq = [-1] * len(s)
        seen = set()
        for idx in range(len(s)):
            if s[idx] not in seen:
                if idx == seq[idx]:
                    return idx
                seen.add(s[idx])
        return -1
