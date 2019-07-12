class Solution(object):

    def lengthOfLongestSubstring_brute(self, s):
        """
        Given a string, find the length of the longest substring without repeating characters.

        Brute force solution, O(n^2) time complexity.


        Parameters
        ----------
        s : str


        Returns
        -------
        ret : int

        """

        ret = 0
        for start in range(len(s)):
            for end in range(start, len(s)):
                test = s[start:end + 1]
                if len(test) == len("".join(set(test))):
                    if len(test) > ret:
                        ret = len(test)
        return ret

    def lengthOfLongestSubstring(self, s):
        """
        Given a string, find the length of the longest substring without repeating characters.

        DP solution.


        Runtime: 1592 ms, faster than 5.00% of Python3 online submissions for Longest Substring Without Repeating Characters.
        Memory Usage: 25.6 MB, less than 5.03% of Python3 online submissions for Longest Substring Without Repeating Characters.


        Parameters
        ----------
        s : str


        Returns
        -------
        ret : int

        """
        ret = 0
        mem = {}

        def iterate(sng):
            nonlocal mem
            nonlocal ret

            max_chunk = len("".join(set(sng)))
            s_len = len(sng)
            if s_len <= ret:
                return 0
            if sng in mem:
                return 0
            else:
                mem[sng] = 1
            if s_len == max_chunk:
                ret = s_len
                return s_len

            return max(map(iterate, [sng[i:i + max_chunk] for i in range(0, len(sng) - max_chunk + 1)]))

        return iterate(s)


if __name__ == "__main__":
    # 3
    Solution().lengthOfLongestSubstring('abcabcbb')
    # 8
    Solution().lengthOfLongestSubstring('qrebtmppwuuhapcegnaon')
    # 9
    Solution().lengthOfLongestSubstring('sarppvkakhasannaeptjdyqpgt')
    # 12
    Solution().lengthOfLongestSubstring('txtuuasalcipqdcfnvybjmynsqlaepaanvujxokkruzhxeokzmnkalxsdisiauinsey')
