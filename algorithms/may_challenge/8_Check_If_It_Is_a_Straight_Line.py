class Solution(object):

    def checkStraightLine(self, coordinates):
        """
        You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point.
        Check if these points make a straight line in the XY plane.

        Constraints:
        2 <= coordinates.length <= 1000
        coordinates[i].length == 2
        -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
        coordinates contains no duplicate point.

        66 / 66 test cases passed.
        Status: Accepted
        Runtime: 64 ms
        Memory Usage: 14.1 MB


        Parameters
        ----------
        coordinates: list


        Returns
        -------
        ret : bool


        Examples
        --------
        >>> Solution().checkStraightLine([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]])
        True

        >>> Solution().checkStraightLine([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]])
        False


        """

        # len guaranteed to be >= 2
        try:
            slope = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
        except ZeroDivisionError:
            slope = float('inf')

        for idx in range(2, len(coordinates)):
            try:
                _n_slope = (coordinates[idx][1] - coordinates[idx - 1][1]) / (coordinates[idx][0] - coordinates[idx - 1][0])
            except ZeroDivisionError:
                _n_slope = float('inf')

            if _n_slope != slope:
                return False

        return True
