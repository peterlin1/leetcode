# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def searchBST(self, root, val):
        """
        Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the
        node's value equals the given value. Return the subtree rooted with that node. If such node doesn't exist, you
        should return NULL.

        Runtime: 80 ms, faster than 58.56% of Python3 online submissions for Search in a Binary Search Tree.
        Memory Usage: 15.7 MB, less than 57.11% of Python3 online submissions for Search in a Binary Search Tree.


        Parameters
        ----------
        root : TreeNode

        val : int


        Returns
        -------
        ret : TreeNode or None

        """

        while root:
            if val == root.val:
                return root
            if val < root.val:
                root = root.left
            else:
                root = root.right
        return None
