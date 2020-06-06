class Solution(object):

    def reconstructQueue(self, people):
        """
        Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers
        (h, k), where h is the height of the person and k is the number of people in front of this person who have a
        height greater than or equal to h. Write an algorithm to reconstruct the queue.

        Note:
        The number of people is less than 1,100.

        Runtime: 184 ms, faster than 30.13% of Python3 online submissions for Queue Reconstruction by Height.
        Memory Usage: 14.3 MB, less than 19.07% of Python3 online submissions for Queue Reconstruction by Height.


        Parameters
        ----------
        people : list


        Returns
        -------
        ret : list


        Examples
        --------
        >>> Solution().reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]])
        [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]

        """

        ret = []
        people.sort(key=lambda p: [-p[0], p[1]])
        for [h, k] in people:
            ret.insert(k, [h, k])
        return ret
