# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def binaryTreePaths(self, root):
        """
        Given a binary tree, return all root-to-leaf paths.


        Parameters
        ----------
        root : TreeNode


        Returns
        -------
        ret : list

        """
        pass


if __name__ == "__main__":
    ex = TreeNode(1)
    a = TreeNode(2)
    b = TreeNode(3)
    c = TreeNode(5)
    ex.left = a
    ex.right = b
    a.left = c

    Solution().binaryTreePaths(ex)
