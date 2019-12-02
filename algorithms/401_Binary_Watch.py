class Solution(object):

    def readBinaryWatch(self, num):
        """
        A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent
        the minutes (0-59).

        Each LED represents a zero or one, with the least significant bit on the right.

        Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible
        times the watch could represent.

        Note:
        The order of output does not matter.
        The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
        The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it
        should be "10:02".

        Runtime: 28 ms, faster than 96.29% of Python3 online submissions for Binary Watch.
        Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Binary Watch.


        Parameters
        ----------
        num : int


        Returns
        -------
        ret : list


        Examples
        --------
        >>> Solution().readBinaryWatch(1)
        ['1:00', '2:00', '4:00', '8:00', '0:01', '0:02', '0:04', '0:08', '0:16', '0:32']

        """

        ret = []

        def _iterator(i_num, i_hr, i_min, hrs, minutes):
            if hrs > 11 or minutes > 59:
                return
            if i_num is 0:
                ret.append(self.read_time(hrs, minutes))
                return
            for h_hr in range(i_hr, 4):
                _iterator(i_num - 1, h_hr + 1, 6, hrs + (1 << h_hr), minutes)
            for m_min in range(i_min, 6):
                _iterator(i_num - 1, i_hr, m_min + 1, hrs, minutes + (1 << m_min))

        _iterator(num, 0, 0, 0, 0)
        return ret

    @staticmethod
    def read_time(hr, minute):
        gap = "0" if minute < 10 else ""
        return """{}:{}{}""".format(hr, gap, minute)

