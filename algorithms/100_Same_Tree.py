# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def isSameTree(self, p, q):
        """
        Given two binary trees, write a function to check if they are the same or not.

        Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

        Runtime: 40 ms, faster than 39.27% of Python3 online submissions for Same Tree.
        Memory Usage: 13.8 MB, less than 5.72% of Python3 online submissions for Same Tree.


        Parameters
        ----------
        p : TreeNode

        q : TreeNode


        Returns
        -------
        ret : bool

        """

        if p and q:
            if p.val != q.val:
                return False
            else:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return p == q
