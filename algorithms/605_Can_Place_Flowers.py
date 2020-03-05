class Solution(object):

    def canPlaceFlowers(self, flowerbed, n):
        """
        Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers
        cannot be planted in adjacent plots - they would compete for water and both would die.

        Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a
        number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.


        Note:
        The input array won't violate no-adjacent-flowers rule.
        The input array size is in the range of [1, 20000].
        n is a non-negative integer which won't exceed the input array size.

        Runtime: 168 ms, faster than 91.04% of Python3 online submissions for Can Place Flowers.
        Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Can Place Flowers.


        Parameters
        ----------
        flowerbed : list

        n : int


        Returns
        -------
        ret : bool


        Examples
        --------
        >>> Solution().canPlaceFlowers([1, 0, 0, 0, 1])
        True

        >>> Solution().canPlaceFlowers([1, 0, 0, 0, 1])
        False

        """

        def _proximity_check(pos):
            if (pos > 0) and (flowerbed[pos - 1] is 1):
                return False

            try:
                if flowerbed[pos + 1] is 1:
                    return False
            except IndexError:
                pass

            return True

        if n is 0:
            return True

        for idx in range(len(flowerbed)):
            if n is 0:
                return True

            if flowerbed[idx] is 0:
                if _proximity_check(idx):
                    flowerbed[idx] = 1
                    n -= 1

        if n is 0:
            return True
        return False
