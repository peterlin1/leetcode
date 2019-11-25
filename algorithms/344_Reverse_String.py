class Solution(object):

    def reverseString(self, s):
        """
        Write a function that reverses a string. The input string is given as an array of characters char[].

        Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1)
        extra memory.

        You may assume all the characters consist of printable ascii characters.


        Runtime: 216 ms, faster than 91.34% of Python3 online submissions for Reverse String.
        Memory Usage: 17.3 MB, less than 97.67% of Python3 online submissions for Reverse String.


        Parameters
        ----------
        s : list


        Examples
        -------
        >>> hello = ["h", "e", "l", "l", "o"]
        >>> Solution().reverseString(hello)
        >>> print(hello)
        ["o","l","l","e","h"]

        """

        for idx in range(len(s) // 2):
            t_s = s[idx]
            s[idx] = s[-1 - idx]
            s[-1 - idx] = t_s


if __name__ == "__main__":
    hello = ["h", "e", "l", "l", "o"]
    Solution().reverseString(hello)
    print(hello)
