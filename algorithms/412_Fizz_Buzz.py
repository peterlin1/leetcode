class Solution(object):

    def fizzBuzz(self, n):
        """
        Write a program that outputs the string representation of numbers from 1 to n.

        But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output
        “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

        Runtime: 44 ms, faster than 79.25% of Python3 online submissions for Fizz Buzz.
        Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Fizz Buzz.


        Parameters
        ----------
        n : int


        Returns
        -------
        ret : list


        Examples
        --------
        >>> Solution().fizzBuzz(15)
        ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']

        """

        ret = ["Fizz"] * n
        for idx in range(n):
            val = idx + 1
            if val % 3 is 0 and val % 5 is 0:
                ret[idx] = 'FizzBuzz'
            elif val % 3 is 0:
                pass
            elif val % 5 is 0:
                ret[idx] = 'Buzz'
            else:
                ret[idx] = str(val)
        return ret


if __name__ == "__main__":
    print(Solution().fizzBuzz(15))
