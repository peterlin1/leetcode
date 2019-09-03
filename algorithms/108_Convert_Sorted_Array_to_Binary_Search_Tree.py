# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def sortedArrayToBST(self, nums):
        """
        Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

        For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two
        subtrees of every node never differ by more than 1.

        Example:

        Given the sorted array: [-10,-3,0,5,9],

        One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

              0
             / \
           -3   9
           /   /
         -10  5

        Runtime: 80 ms, faster than 54.91% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
        Memory Usage: 16.1 MB, less than 6.45% of Python3 online submissions for Convert Sorted Array to Binary Search
        Tree.


        Parameters
        ----------
        nums : list


        Returns
        -------
        ret : TreeNode

        """
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])

        # Also works but is on average slower
        # if len(nums) <= 1:
        #     try:
        #         return TreeNode(nums[0])
        #     except IndexError:
        #         return None

        _mp = len(nums) // 2
        ret = TreeNode(nums[_mp])
        ret.left = self.sortedArrayToBST(nums[:_mp])
        ret.right = self.sortedArrayToBST(nums[_mp + 1:])
        return ret
