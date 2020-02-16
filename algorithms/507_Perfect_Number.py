class Solution(object):
    def checkPerfectNumber(self, num):
        """
        We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except
        itself.

        Now, given an integer n, write a function that returns true when it is a perfect number and false when it is
        not.

        Note: The input number n will not exceed 100,000,000. (1e8)

        Runtime: 40 ms, faster than 40.17% of Python3 online submissions for Perfect Number.
        Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Perfect Number.


        Parameters
        ----------
        num : int

        Returns
        -------
        ret : bool


        Examples
        --------
        >>> Solution().checkPerfectNumber(28)
        True

        """

        if num <= 1:
            return False

        sum_num = 1

        sqrt = num / 2
        while sqrt != num:
            n_ret = sqrt - (((sqrt ** 2) - num) / (2 * sqrt))
            if int(n_ret) == int(sqrt):
                sqrt = int(sqrt)
                break
            else:
                sqrt = n_ret
        sqrt = int(sqrt)

        n = 2
        while n < sqrt + 1:
            if num % n is 0:
                sum_num += n + int(num / n)
                if sum_num > num:
                    return False
            n += 1

        if sum_num == num:
            return True
        return False
