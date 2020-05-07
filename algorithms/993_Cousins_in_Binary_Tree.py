# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def isCousins(self, root, x, y):
        """
        In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

        Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

        We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the
        tree.

        Return true if and only if the nodes corresponding to the values x and y are cousins.

        Note:
        The number of nodes in the tree will be between 2 and 100.
        Each node has a unique integer value from 1 to 100.

        Runtime: 20 ms, faster than 99.49% of Python3 online submissions for Cousins in Binary Tree.
        Memory Usage: 14.1 MB, less than 6.12% of Python3 online submissions for Cousins in Binary Tree.


        Parameters
        ----------
        root : TreeNode

        x : int

        y : int


        Returns
        -------
        ret : bool

        """

        queue = [(root, 0, None)]
        found = []

        while queue and len(found) < 2:
            s_node = queue.pop(0)
            # print(s_node[0].val)

            if s_node[0].left:
                if (s_node[0].left.val == x) or (s_node[0].left.val == y):
                    found.append((s_node[0].left, s_node[1] + 1, s_node[0]))
                else:
                    queue.append((s_node[0].left, s_node[1] + 1, s_node[0]))
            if s_node[0].right:
                if (s_node[0].right.val == x) or (s_node[0].right.val == y):
                    found.append((s_node[0].right, s_node[1] + 1, s_node[0]))
                else:
                    queue.append((s_node[0].right, s_node[1] + 1, s_node[0]))

        if len(found) != 2:
            return False
        return (found[0][2] != found[1][2]) and (found[0][1] == found[1][1])


if __name__ == "__main__":
    ex1 = TreeNode(1)
    a = TreeNode(2)
    b = TreeNode(3)
    c = TreeNode(4)
    d = TreeNode(5)

    ex1.left = a
    ex1.right = b
    a.right = c
    b.right = d

    print(Solution().isCousins(ex1, 5, 4))
