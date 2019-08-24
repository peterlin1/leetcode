# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the
        nodes of the first two lists.

        Runtime: 44 ms, faster than 64.33% of Python3 online submissions for Merge Two Sorted Lists.
        Memory Usage: 13.8 MB, less than 6.61% of Python3 online submissions for Merge Two Sorted Lists.


        Parameters
        ----------
        l1 : ListNode

        l2 : ListNode


        Returns
        -------
        ret : ListNode

        """
        ret = ret_pointer = ListNode(0)
        while l1 or l2:
            if (l1 and l2 is None) or (l1 and l1.val <= l2.val):
                ret_pointer.next = l1
                l1 = l1.next
            else:
                ret_pointer.next = l2
                l2 = l2.next
            ret_pointer = ret_pointer.next

        return ret.next


def int_to_listnode(num):
    ret_pointer = ret = ListNode(None)
    num_str = str(num)

    for digit in num_str:
        ret_pointer.next = ListNode(int(digit))
        ret_pointer = ret_pointer.next
    return ret.next


def print_listnode(ln):
    ret = []
    while ln:
        ret.append(ln.val)
        ln = ln.next
    print(ret)


if __name__ == "__main__":
    l1 = int_to_listnode(124)
    l2 = int_to_listnode(134)

    ex = Solution().mergeTwoLists(l1, l2)
    print_listnode(ex)
