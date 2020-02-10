class Solution(object):

    def findRadius(self, houses, heaters):
        """
        Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to
        warm all the houses.

        Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so
        that all houses could be covered by those heaters.

        So, your input will be the positions of houses and heaters seperately, and your expected output will be the
        minimum radius standard of heaters.

        Note:

        Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
        Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
        As long as a house is in the heaters' warm radius range, it can be warmed.
        All the heaters follow your radius standard and the warm radius will the same.

        Runtime: 320 ms, faster than 43.61% of Python3 online submissions for Heaters.
        Memory Usage: 16 MB, less than 16.67% of Python3 online submissions for Heaters.


        Parameters
        ----------
        houses : list

        heaters : list


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().findRadius([1, 2, 3], [2])
        1

        >>> Solution().findRadius([1, 2, 3, 4], [1, 4])
        1

        """

        if (len(houses) is 0) or (len(heaters) is 0):
            return 0

        houses.sort()
        heaters.sort()
        ret = 0
        pos = 0

        for house in houses:
            h_span = (heaters[pos] - ret, heaters[pos] + ret)
            if house < h_span[0]:
                ret = max(ret, heaters[pos] - house)
            elif house > h_span[1]:
                while pos < len(heaters):
                    if heaters[pos] < house:
                        pos += 1
                    else:
                        break
                pos -= 1
                try:
                    ret = max(ret, min(house - heaters[pos], heaters[pos + 1] - house))
                except IndexError:
                    ret = max(ret, house - heaters[pos])
        return ret
