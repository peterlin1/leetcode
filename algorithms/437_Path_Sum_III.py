# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def pathSum(self, root, sum):
        """
        You are given a binary tree in which each node contains an integer value.

        Find the number of paths that sum to a given value.

        The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from
        parent nodes to child nodes).

        The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

        Runtime: 48 ms, faster than 88.25% of Python3 online submissions for Path Sum III.
        Memory Usage: 15 MB, less than 6.82% of Python3 online submissions for Path Sum III.


        Parameters
        ----------
        root : TreeNode

        sum : int


        Returns
        -------
        ret : int

        """

        self.ret = 0
        self.mem = {sum: 1}

        def _traverse(node, rem):
            if not node:
                return

            rem -= node.val
            self.ret += self.mem.get(rem + sum, 0)
            self.mem[rem] = self.mem.get(rem, 0) + 1

            _traverse(node.left, rem)
            _traverse(node.right, rem)
            self.mem[rem] -= 1

        _traverse(root, sum)
        return self.ret


if __name__ == "__main__":
    # ex1 = TreeNode(10)
    # a = TreeNode(5)
    # b = TreeNode(-3)
    # c = TreeNode(3)
    # d = TreeNode(2)
    # e = TreeNode(11)
    # f = TreeNode(3)
    # g = TreeNode(-2)
    # h = TreeNode(1)
    #
    # ex1.left = a
    # ex1.right = b
    # a.left = c
    # a.right = d
    # b.right = e
    # c.left = f
    # c.right = g
    # d.right = h

    ex1 = TreeNode(1)
    a = TreeNode(2)
    b = TreeNode(3)
    c = TreeNode(1)
    d = TreeNode(2)

    ex1.right = a
    a.right = b
    b.right = c
    c.right = d
    print(Solution().pathSum(ex1, 3))
