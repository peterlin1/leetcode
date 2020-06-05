import random


class Solution(object):

    def __init__(self, w):
        """
        Parameters
        ----------
        w : list

        """

        self.population = 0
        self.prob = []

        for idx in w:
            self.population += idx
            self.prob.append(self.population)

    def pickIndex(self):
        """
        Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex
        which randomly picks an index in proportion to its weight.

        Explanation of Input Syntax:
        The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the
        array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any

        Note:
        1 <= w.length <= 10000
        1 <= w[i] <= 10^5
        pickIndex will be called at most 10000 times.

        57 / 57 test cases passed.
        Status: Accepted
        Runtime: 328 ms
        Memory Usage: 18.2 MB


        Returns
        -------
        ret : int
        """

        # return random.choices(self.population, self.w)[0]
        card = random.randint(1, self.population)
        left = 0
        right = len(self.prob)

        while left < right:
            mid = left + (right - left) // 2
            if self.prob[mid] == card:
                return mid
            elif self.prob[mid] < card:
                left = mid + 1
            else:
                right = mid
        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
if __name__ == "__main__":
    ex1 = Solution([3, 5, 6, 7])
    ex1.pickIndex()

