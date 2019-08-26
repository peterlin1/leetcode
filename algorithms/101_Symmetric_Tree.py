# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def isSymmetric(self, root):
        """
        Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

        Runtime: 36 ms, faster than 92.49% of Python3 online submissions for Symmetric Tree.
        Memory Usage: 13.8 MB, less than 5.17% of Python3 online submissions for Symmetric Tree.


        Parameters
        ----------
        root : TreeNode


        Returns
        -------
        ret : bool

        """

        def _isSymmetric(left, right):
            if not left and not right:
                return True
            elif not left or not right:
                return False
            elif left.val != right.val:
                return False
            try:
                return _isSymmetric(left.right, right.left) and _isSymmetric(left.left, right.right)
            except AttributeError:
                return False

        if not root:
            return True
        else:
            return _isSymmetric(root.left, root.right)


if __name__ == "__main__":
    ex = TreeNode(1)
    ex.left = TreeNode(2)
    ex.right = TreeNode(2)

    ex.left.left = TreeNode(3)
    ex.left.right = TreeNode(4)

    ex.right.left = TreeNode(4)
    # ex.right.right = TreeNode(3)

    print(Solution().isSymmetric(ex))
