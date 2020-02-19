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

        Runtime: 32 ms, faster than 54.23% of Python3 online submissions for Binary Tree Paths.
        Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Binary Tree Paths.


        Parameters
        ----------
        root : TreeNode


        Returns
        -------
        ret : list

        """

        ret = []

        def _traverse(node, pre):
            if node.left and node.right:
                _traverse(node.left, """{}->{}""".format(pre, node.val))
                _traverse(node.right, """{}->{}""".format(pre, node.val))
            elif node.left:
                _traverse(node.left, """{}->{}""".format(pre, node.val))
            elif node.right:
                _traverse(node.right, """{}->{}""".format(pre, node.val))
            else:
                ret.append("""{}->{}""".format(pre, node.val))

        if not root:
            return ret
        if not root.left and not root.right:
            return [str(root.val)]
        if root.left:
            _traverse(root.left, str(root.val))
        if root.right:
            _traverse(root.right, str(root.val))

        return ret


if __name__ == "__main__":
    ex = TreeNode(1)
    a = TreeNode(2)
    b = TreeNode(3)
    c = TreeNode(5)
    ex.left = a
    ex.right = b
    a.left = c

    print(Solution().binaryTreePaths(ex))
