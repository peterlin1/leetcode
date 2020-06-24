# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def countNodes(self, root):
        """
        Given a complete binary tree, count the number of nodes.

        Note:
        Definition of a complete binary tree from Wikipedia:
        In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last
        level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

        Runtime: 92 ms, faster than 50.29% of Python3 online submissions for Count Complete Tree Nodes.
        Memory Usage: 21.2 MB, less than 49.82% of Python3 online submissions for Count Complete Tree Nodes.


        Parameters
        ----------
        root : TreeNode


        Returns
        -------
        ret : int

        """

        if not root:
            return 0

        queue = [root]
        ret = 0

        while queue:
            node = queue.pop()
            ret += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return ret


if __name__ == "__main__":
    ex1 = TreeNode(1)
    a = TreeNode(2)
    b = TreeNode(3)
    c = TreeNode(4)
    d = TreeNode(5)
    e = TreeNode(6)

    ex1.left = a
    ex1.right = b
    a.left = c
    a.right = d
    b.left = e

    print(Solution().countNodes(ex1))
