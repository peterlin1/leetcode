# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def __init__(self):
        self.ret = 0

    def diameterOfBinaryTree(self, root):
        """
        Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree
        is the length of the longest path between any two nodes in a tree. This path may or may not pass through the
        root.

        Note: The length of path between two nodes is represented by the number of edges between them.

        Runtime: 36 ms, faster than 97.05% of Python3 online submissions for Diameter of Binary Tree.
        Memory Usage: 15.7 MB, less than 58.62% of Python3 online submissions for Diameter of Binary Tree.


        Parameters
        ----------
        root : TreeNode


        Returns
        -------
        ret : int

        """

        self.ret = 0

        def _max_length(node):
            if not node:
                return 0
            _l_ret = _max_length(node.left)
            _r_ret = _max_length(node.right)
            self.ret = max(self.ret, _r_ret + _l_ret)
            return 1 + max(_l_ret, _r_ret)

        _max_length(root)
        return self.ret


if __name__ == "__main__":
    root = TreeNode(1)
    a = TreeNode(2)
    b = TreeNode(3)
    c = TreeNode(4)
    d = TreeNode(5)

    root.left = a
    root.right = b
    a.left = c
    a.right = d

    Solution().diameterOfBinaryTree(root)
