# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def invertTree(self, root):
        """
        Invert a binary tree.

        68 / 68 test cases passed.
        Status: Accepted
        Runtime: 24 ms
        Memory Usage: 13.9 MB


        Example:

        Input:

             4
           /   \
          2     7
         / \   / \
        1   3 6   9
        Output:

             4
           /   \
          7     2
         / \   / \
        9   6 3   1


        Parameters
        ----------
        root : TreeNode


        Returns
        -------
        ret : TreeNode

        """

        def _inv(node):
            if node and (node.left or node.right):
                t_n = node.left
                node.left = node.right
                node.right = t_n
                _inv(node.left)
                _inv(node.right)

        if root:
            pointer = root
            _inv(pointer)
        return root


if __name__ == "__main__":
    a = TreeNode(4)
    b = TreeNode(2)
    c = TreeNode(7)
    d = TreeNode(1)
    e = TreeNode(3)
    f = TreeNode(6)
    g = TreeNode(9)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g

    Solution().invertTree(a)
