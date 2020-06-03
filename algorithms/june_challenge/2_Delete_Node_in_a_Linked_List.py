# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteNode(self, node):
        """
        Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

        The linked list will have at least two elements.
        All of the nodes' values will be unique.
        The given node will not be the tail and it will always be a valid node of the linked list.
        Do not return anything from your function.

        41 / 41 test cases passed.
        Status: Accepted
        Runtime: 36 ms
        Memory Usage: 14.2 MB


        Parameters
        ----------
        node : ListNode

        """

        while node and node.next:
            node.val = node.next.val
            if not node.next.next:
                node.next = None
            else:
                node = node.next
