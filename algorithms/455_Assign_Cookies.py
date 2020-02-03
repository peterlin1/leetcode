class Solution(object):

    def findContentChildren(self, g, s):
        """
        Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at
        most one cookie. Each child i has a greed factor gi, which is the minimum size of a cookie that the child will
        be content with; and each cookie j has a size sj. If sj >= gi, we can assign the cookie j to the child i, and
        the child i will be content. Your goal is to maximize the number of your content children and output the maximum
        number.

        Note:
        You may assume the greed factor is always positive.
        You cannot assign more than one cookie to one child.

        Runtime: 168 ms, faster than 90.54% of Python3 online submissions for Assign Cookies.
        Memory Usage: 14.6 MB, less than 42.86% of Python3 online submissions for Assign Cookies.


        Parameters
        ----------
        g : list

        s : list


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().findContentChildren([1, 2, 3], [1, 1])
        1

        >>> Solution().findContentChildren([1, 2], [1, 2, 3])
        2

        >>> Solution().findContentChildren([1, 1, 2, 2, 5], [1, 1, 1, 2, 6])
        4

        """

        g = sorted(g)
        s = sorted(s)

        idx_g = len(g) - 1
        idx_s = len(s) - 1

        while idx_g >= 0 and idx_s >= 0:
            if s[idx_s] >= g[idx_g]:
                idx_s -= 1
            idx_g -= 1
        return len(s) - idx_s - 1
