class Solution(object):

    def countAndSay(self, n):
        """
        The count-and-say sequence is the sequence of integers with the first five terms as following:

        1.     1
        2.     11
        3.     21
        4.     1211
        5.     111221
        1 is read off as "one 1" or 11.
        11 is read off as "two 1s" or 21.
        21 is read off as "one 2, then one 1" or 1211.

        Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

        Note: Each term of the sequence of integers will be represented as a string.

        Runtime: 44 ms, faster than 43.09% of Python3 online submissions for Count and Say.
        Memory Usage: 13.9 MB, less than 6.38% of Python3 online submissions for Count and Say.


        Parameters
        ----------
        n : int

        Returns
        -------
        ret : str


        Examples
        --------
        >>> Solution().countAndSay(1)
        '1'

        >>> Solution().countAndSay(4)
        '1211'

        >>> Solution().countAndSay(10)
        13211311123113112211

        """

        if n == 1:
            return "1"
        else:
            p_seq = self.countAndSay(n - 1)
            count = 0
            say = p_seq[0]
            ret = ""
            for val in p_seq:
                if val == say:
                    count += 1
                else:
                    ret = ret + str(count) + str(say)
                    say = val
                    count = 1
            ret = ret + str(count) + str(say)
            return ret


if __name__ == "__main__":
    print(Solution().countAndSay(10))
