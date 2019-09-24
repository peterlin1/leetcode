# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def lowestCommonAncestor(self, root, p, q):
        """
        Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

        According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and
        q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of
        itself).”


        Parameters
        ----------
        root
        p
        q

        Returns
        -------

        """

        pass


if __name__ == "__main__":
    ex1 = TreeNode(6)
    a = TreeNode(2)
    b = TreeNode(0)
    c = TreeNode(4)
    d = TreeNode(3)
    e = TreeNode(5)
    f = TreeNode(8)
    g = TreeNode(7)
    h = TreeNode(9)

    ex1.left = a
    ex1.right = f
    a.left = b
    a.right = c
    c.left = d
    c.right = e
    f.left = g
    f.right = h
    print(Solution().lowestCommonAncestor(ex1))
