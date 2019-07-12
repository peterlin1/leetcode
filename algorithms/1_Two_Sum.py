class Solution:

    def twoSum(self, nums, target):
        """
        Given an array of integers, return indices of the two numbers such that they add up to a specific target.

        You may assume that each input would have exactly one solution, and you may not use the same element twice.

        Runtime: 60 ms, faster than 39.98% of Python3 online submissions for Two Sum.
        Memory Usage: 14.9 MB, less than 12.21% of Python3 online submissions for Two Sum.


        Parameters
        ----------
        nums : list
        target : int


        Examples
        --------
        >>> nums = [2, 7, 11, 15]
        >>> target = 9
        >>> Solution().twoSum(nums=nums, target=9)
        [0, 1]


        Returns
        -------
        ret : list

        """
        enum_nums = list(enumerate(nums))
        enum_nums.sort(key=lambda x: x[1])
        enum_nums_search = enum_nums.copy()

        # print(enum_nums)
        ret = list()
        for idx, enum_num in enum_nums:
            # print("""idx: {}  num: {}""".format(idx, enum_num))
            enum_nums_search.pop(0)
            # print("""Searching for {} in {}""".format(target - enum_num, enum_nums_search))
            idy = next((v[0] for i, v in enumerate(enum_nums_search) if v[1] == target - enum_num), None)
            if idy is None:
                continue
            # print("""Found idy {}""".format(idy))

            ret = [idx, idy]
            ret.sort()
            break

        return ret


if __name__ == "__main__":
    # [0,1]
    Solution().twoSum(nums=[2, 7, 11, 15], target=9)
    # [2,3]
    Solution().twoSum(nums=[8, 2, 11, 7, 15], target=18)
    # [0,1]
    Solution().twoSum(nums=[3, 3], target=6)
