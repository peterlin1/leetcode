# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def isPalindrome(self, head):
        """
        Given a singly linked list, determine if it is a palindrome.

        Runtime: 84 ms, faster than 37.27% of Python3 online submissions for Palindrome Linked List.
        Memory Usage: 24.2 MB, less than 7.69% of Python3 online submissions for Palindrome Linked List.


        Parameters
        ----------
        head : ListNode


        Returns
        -------
        ret : bool

        """

        if not head:
            return True
        if not head.next:
            return True
        try:
            hare = head.next.next
        except AttributeError:
            if head.val == head.next.val:
                return True
            return False
        tortoise = head.next
        head.next = None
        while hare and hare.next:
            n_p = tortoise.next
            tortoise.next = head
            head = tortoise
            tortoise = n_p
            hare = hare.next.next
        # Odd number of nodes
        if hare:
            tortoise = tortoise.next
        while head:
            if head.val != tortoise.val:
                return False
            head = head.next
            tortoise = tortoise.next
        return True


if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(2)
    d = ListNode(1)

    a.next = b
    b.next = c
    c.next = d

    print(Solution().isPalindrome(a))

    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(2)
    e = ListNode(1)

    a.next = b
    b.next = c
    c.next = d
    d.next = e

    print(Solution().isPalindrome(a))