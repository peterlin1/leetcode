# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def kthSmallest(self, root, k):
        """
        Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

        Note:
        You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

        Follow up:
        What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently?
        How would you optimize the kthSmallest routine?

        91 / 91 test cases passed.
        Status: Accepted
        Runtime: 48 ms
        Memory Usage: 17.8 MB


        Parameters
        ----------
        root : TreeNode

        k : int


        Returns
        -------
        ret : int

        """

        self.level = k

        def _in_order(node):
            if node:
                l_val = _in_order(node.left)
                if l_val is not None:
                    return l_val
                # print(node.val, self.level)
                if self.level == 1:
                    return node.val
                self.level -= 1
                r_val = _in_order(node.right)
                if r_val is not None:
                    return r_val

        return _in_order(root)


if __name__ == "__main__":
    ex1 = TreeNode(31)
    a = TreeNode(30)
    b = TreeNode(48)
    c = TreeNode(3)
    d = TreeNode(38)
    e = TreeNode(49)
    f = TreeNode(0)

    ex1.left = a
    ex1.right = b
    a.left = c
    b.left = d
    b.right = e
    c.left = f

    Solution().kthSmallest(ex1, 2)
