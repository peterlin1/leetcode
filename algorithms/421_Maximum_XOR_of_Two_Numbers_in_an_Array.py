class Solution(object):

    def findMaximumXOR(self, nums):
        """
        Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

        Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

        Could you do this in O(n) runtime?

        Runtime: 1348 ms, faster than 5.01% of Python3 online submissions for Maximum XOR of Two Numbers in an Array.
        Memory Usage: 151.4 MB, less than 100.00% of Python3 online submissions for Maximum XOR of Two Numbers in an Array.


        Parameters
        ----------
        nums : list


        Returns
        -------
        ret : int


        Examples
        --------
        >>> Solution().findMaximumXOR([3, 10, 5, 25, 2, 8])
        28

        """
        ret = 0
        mem = Trie()

        for dec in nums:
            n_xor = mem.insert(format(dec, '032b'), dec)
            ret = max(ret, (n_xor ^ dec))
        return ret


class TrieNode:

    def __init__(self, dec=None):
        """

        Parameters
        ----------
        dec int

        """
        self.children = {}
        self.dec = dec
        self.end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, bin_val, dec):
        pointer = d_pointer = self.root
        for bit in bin_val:
            if bit in pointer.children.keys():
                pointer = pointer.children[bit]
            else:
                n_node = TrieNode()
                pointer.children[bit] = n_node
                pointer = n_node

            # toggled bit
            t_bit = str(int(bit) ^ 1)
            if t_bit in d_pointer.children.keys():
                d_pointer = d_pointer.children[t_bit]
            else:
                d_pointer = d_pointer.children[bit]

        pointer.end = True
        pointer.dec = dec
        return d_pointer.dec

    def get_all_nodes(self):
        pointer = self.root
        all_dec = []

        def _get_node(node):
            if node.end:
                all_dec.append(node.dec)
            for k in node.children.values():
                _get_node(k)
        _get_node(pointer)
        return all_dec

    def print_all_nodes(self):
        pointer = self.root

        def _print_node(node):
            if node and pointer.children:
                print(node.children.keys())
                for k in node.children.keys():
                    _print_node(node.children[k])

        _print_node(pointer)


if __name__ == "__main__":
    # testTrie = Trie()
    # testTrie.insert("1001", 9)
    # testTrie.insert("0100", 4)
    #
    # print(testTrie.get_all_nodes())
    # testTrie.print_all_nodes()
    print(Solution().findMaximumXOR([3, 10, 5, 25, 2, 8, 879, 4301]))
