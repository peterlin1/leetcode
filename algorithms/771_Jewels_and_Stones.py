class Solution(object):

    def numJewelsInStones(self, J, S):
        """
        You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
        Each character in S is a type of stone you have.  You want to know how many of the stones you have are also
        jewels.

        The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive,
        so "a" is considered a different type of stone from "A".

        Note:
        S and J will consist of letters and have length at most 50.
        The characters in J are distinct.

        Runtime: 68 ms, faster than 5.31% of Python3 online submissions for Jewels and Stones.
        Memory Usage: 14 MB, less than 5.39% of Python3 online submissions for Jewels and Stones.


        Parameters
        ----------
        J : str

        S : str


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().numJewelsInStones("aA", "aAAbbbb")
        3

        >>> Solution().numJewelsInStones("z", "ZZ")
        0

        """

        return len([val for val in S if val in J])
