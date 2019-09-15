# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def reverseList(self, head):
        """
        Reverse a singly linked list.

        Runtime: 40 ms, faster than 83.43% of Python3 online submissions for Reverse Linked List.
        Memory Usage: 15 MB, less than 31.82% of Python3 online submissions for Reverse Linked List.


        Parameters
        ----------
        head : ListNode


        Returns
        -------
        ret : ListNode

        """

        if not head:
            return
        pointer = head.next
        head.next = None
        while pointer:
            n_p = pointer.next
            pointer.next = head
            head = pointer
            pointer = n_p
        return head


if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    ex1 = Solution().reverseList(a)
    print(ex1.val)
