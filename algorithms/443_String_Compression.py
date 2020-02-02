class Solution(object):

    def compress(self, chars):
        """
        Given an array of characters, compress it in-place.

        The length after compression must always be smaller than or equal to the original array.

        Every element of the array should be a character (not int) of length 1.

        After you are done modifying the input array in-place, return the new length of the array.

        Runtime: 52 ms, faster than 94.01% of Python3 online submissions for String Compression.
        Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for String Compression.


        Parameters
        ----------
        chars

        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().compress(["a", "a", "b", "b", "c", "c", "c"])
        6

        >>> Solution().compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"])
        4

        """

        if len(chars) is 0:
            return 0

        tortoise = 0
        bunny = 1
        cnt = 1
        for idx in range(1, len(chars)):
            # print(idx, tortoise, bunny)
            if chars[tortoise] == chars[idx]:
                cnt += 1
            else:
                if cnt is 1:
                    chars[bunny] = chars[idx]
                    tortoise += 1
                    bunny = tortoise + 1
                else:
                    for dgt in str(cnt):
                        chars[bunny] = dgt
                        bunny += 1
                    tortoise = bunny
                    chars[tortoise] = chars[idx]
                    bunny = tortoise + 1
                cnt = 1
        if cnt > 1:
            for dgt in str(cnt):
                chars[bunny] = dgt
                bunny += 1
        return bunny


if __name__ == "__main__":
    ex1 = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    print(Solution().compress(ex1))
    print(ex1)
