# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sumNumbers(self, root):
        """
        Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

        An example is the root-to-leaf path 1->2->3 which represents the number 123.

        Find the total sum of all root-to-leaf numbers.

        Note: A leaf is a node with no children.

        110 / 110 test cases passed.
        Status: Accepted
        Runtime: 32 ms
        Memory Usage: 14 MB


        Parameters
        ----------
        root : TreeNode


        Returns
        -------
        ret : int

        """

        if not root:
            return 0

        ret = []

        def _iterate(node, digits):
            if not node.left and not node.right:
                ret.append(digits + str(node.val))

            if node.left:
                _iterate(node.left, digits + str(node.val))
            if node.right:
                _iterate(node.right, digits + str(node.val))

        _iterate(root, "")
        # print(ret)
        return sum([int(_) for _ in ret])


if __name__ == "__main__":
    ex1 = TreeNode(4)
    a = TreeNode(9)
    b = TreeNode(0)
    c = TreeNode(5)
    d = TreeNode(1)

    ex1.left = a
    ex1.right = b
    a.left = c
    a.right = d
    Solution().sumNumbers(ex1)
