class Solution(object):

    def checkRecord(self, s):
        """
        You are given a string representing an attendance record for a student. The record only contains the following
        three characters:

        'A' : Absent.
        'L' : Late.
        'P' : Present.

        A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two
        continuous 'L' (late).

        You need to return whether the student could be rewarded according to his attendance record.

        Runtime: 24 ms, faster than 88.63% of Python3 online submissions for Student Attendance Record I.
        Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Student Attendance Record I.


        Parameters
        ----------
        s

        Returns
        -------
        ret : bool


        Examples
        --------
        >>> Solution().checkRecord("PPALLP")
        True

        >>> Solution().checkRecord("PPALLP")
        True

        """

        abst = 0
        c_late = 0
        for val in s:
            if val == 'A':
                if abst is 1:
                    return False
                abst += 1
                c_late = 0
            elif val == 'L':
                if c_late is 2:
                    return False
                c_late += 1
            else:
                c_late = 0
        return True
