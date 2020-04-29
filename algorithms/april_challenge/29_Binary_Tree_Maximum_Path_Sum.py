# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def maxPathSum(self, root):
        """
        Given a non-empty binary tree, find the maximum path sum.

        For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree
        along the parent-child connections. The path must contain at least one node and does not need to go through the
        root.

        93 / 93 test cases passed.
        Status: Accepted
        Runtime: 88 ms
        Memory Usage: 21.1 MB


        Parameters
        ----------
        root

        Returns
        -------
        ret : int

        """

        # root is guaranteed to not be empty
        self.ret = root.val

        def _max_sum(node):
            if not node:
                return 0

            _l_ret = max(_max_sum(node.left), 0)
            _r_ret = max(_max_sum(node.right), 0)
            self.ret = max(self.ret, node.val + _l_ret + _r_ret)
            return node.val + max(_l_ret, _r_ret)

        _max_sum(root)
        return self.ret


if __name__ == "__main__":
    ex1 = TreeNode(-10)
    a = TreeNode(9)
    b = TreeNode(20)
    c = TreeNode(15)
    d = TreeNode(7)

    ex1.left = a
    ex1.right = b
    b.left = c
    b.right = d
    #
    # ex1 = TreeNode(1)
    # a = TreeNode(2)
    # b = TreeNode(3)
    #
    # ex1.left = a
    # ex1.right = b

    print(Solution().maxPathSum(ex1))
