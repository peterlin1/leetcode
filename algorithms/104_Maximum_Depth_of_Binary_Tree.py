# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def maxDepth(self, root):
        """
        Given a binary tree, find its maximum depth.

        The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf
        node.

        Note: A leaf is a node with no children.

        Runtime: 52 ms, faster than 44.88% of Python3 online submissions for Maximum Depth of Binary Tree.
        Memory Usage: 16.3 MB, less than 5.21% of Python3 online submissions for Maximum Depth of Binary Tree.


        Parameters
        ----------
        root : TreeNode


        Returns
        -------
        ret : int

        """

        if root:
            if not root.left and not root.right:
                return 1
            elif root.left and root.right:
                return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
            elif root.left:
                return self.maxDepth(root.left) + 1
            else:
                return self.maxDepth(root.right) + 1
        else:
            return 0
