# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def removeElements(self, head, val):
        """
        Remove all elements from a linked list of integers that have value val.

        Runtime: 80 ms, faster than 38.83% of Python3 online submissions for Remove Linked List Elements.
        Memory Usage: 16.9 MB, less than 5.55% of Python3 online submissions for Remove Linked List Elements.


        Parameters
        ----------
        head : ListNode

        val : int


        Returns
        -------
        ret : ListNode

        """
        ret = head
        try:
            pointer = head.next
        except AttributeError:
            return head
        while pointer:
            if pointer.val == val:
                ret.next = pointer.next
            else:
                ret = ret.next
            pointer = pointer.next
        if head.val == val:
            return head.next
        return head
