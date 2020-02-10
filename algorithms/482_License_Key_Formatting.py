class Solution(object):

    def licenseKeyFormatting(self, S, K):
        """
        ou are given a license key represented as a string S which consists only alphanumeric character and dashes. The
        string is separated into N+1 groups by N dashes.

        Given a number K, we would want to reformat the strings such that each group contains exactly K characters,
        except for the first group which could be shorter than K, but still must contain at least one character.
        Furthermore, there must be a dash inserted between two groups and all lowercase letters should be converted to
        uppercase.

        Given a non-empty string S and a number K, format the string according to the rules described above.

        Note:
        The length of string S will not exceed 12,000, and K is a positive integer.
        String S consists only of alphanumerical characters (a-z and/or A-Z and/or 0-9) and dashes(-).
        String S is non-empty.

        Runtime: 44 ms, faster than 70.10% of Python3 online submissions for License Key Formatting.
        Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for License Key Formatting.


        Parameters
        ----------
        S : str

        K : int

        Returns
        -------
        ret : str


        Examples
        --------
        >>> Solution().licenseKeyFormatting("5F3Z-2e-9-w", 4)
        "5F3Z-2E9W"

        """

        pt_s = S.replace('-', '').upper()
        if not len(pt_s):
            return ""
        l_g = len(pt_s) % K
        if l_g > 0:
            ret = pt_s[0:l_g]
        for idx in range(len(pt_s) // K):
            print("""{} {}""".format(idx * K + l_g, idx * K + K + l_g))
            try:
                ret += '-' + pt_s[idx * K + l_g:idx * K + K + l_g]
            except UnboundLocalError:
                ret = pt_s[idx * K + l_g:idx * K + K + l_g]

        return ret
