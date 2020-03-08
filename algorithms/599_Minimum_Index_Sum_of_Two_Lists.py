class Solution(object):

    def findRestaurant(self, list1, list2):
        """
        Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants
        represented by strings.

        You need to help them find out their common interest with the least list index sum. If there is a choice tie
        between answers, output all of them with no order requirement. You could assume there always exists an answer.

        Note:
        The length of both lists will be in the range of [1, 1000].
        The length of strings in both lists will be in the range of [1, 30].
        The index is starting from 0 to the list length minus 1.
        No duplicates in both lists.

        Runtime: 148 ms, faster than 94.54% of Python3 online submissions for Minimum Index Sum of Two Lists.
        Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Minimum Index Sum of Two Lists.


        Parameters
        ----------
        list1 : list

        list2 : list


        Returns
        -------
        ret : list


        Examples
        --------
        >>> Solution().findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],
        ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"])
        ["Shogun"]

        >>> Solution().findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],
        ["KFC", "Shogun", "Burger King"])
        ["Shogun"]
        """

        min_idx = len(list1) + len(list2) - 2
        dict_l1 = {k: v for v, k in enumerate(list1)}
        ret = []

        for idx in range(len(list2)):
            try:
                n_m = dict_l1[list2[idx]] + idx
            except KeyError:
                continue
            if n_m == min_idx:
                ret.append(list2[idx])
            elif n_m < min_idx:
                ret = [list2[idx]]
                min_idx = n_m

        return ret
