# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def deleteDuplicates(self, head):
        """
        Given a sorted linked list, delete all duplicates such that each element appear only once.

        Runtime: 52 ms, faster than 34.46% of Python3 online submissions for Remove Duplicates from Sorted List.
        Memory Usage: 13.9 MB, less than 6.45% of Python3 online submissions for Remove Duplicates from Sorted List.


        Parameters
        ----------
        head : ListNode


        Returns
        -------
        ret : ListNode

        """
        ret = ret_pointer = head
        while head:
            if head.val == ret_pointer.val:
                ret_pointer.next = head.next
            else:
                ret_pointer.next = head
                ret_pointer = ret_pointer.next
            head = head.next
        return ret


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
    l1 = int_to_listnode(1111)

    ex = Solution().deleteDuplicates(l1)
    print_listnode(ex)
