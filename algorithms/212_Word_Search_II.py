class TrieNode:

    def __init__(self):
        self.children = [None] * 26
        self.end = False
        self.word = None


class Solution(object):

    @staticmethod
    def trie(words):
        ret = TrieNode()
        for word in words:
            temp = ret
            for char in word:
                n_char = ord(char) - 97
                if not temp.children[n_char]:
                    temp.children[n_char] = TrieNode()
                temp = temp.children[n_char]
            temp.word = word
            temp.end = True
        return ret

    def findWords(self, board, words):
        """
        Given a 2D board and a list of words from the dictionary, find all words in the board.

        Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those
        horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

        Runtime: 328 ms, faster than 75.64% of Python3 online submissions for Word Search II.
        Memory Usage: 37.8 MB, less than 7.08% of Python3 online submissions for Word Search II.


        Parameters
        ----------
        board : list

        words : list


        Returns
        -------
        ret : list


        Examples
        --------
        >>> Solution().findWords([["o", "a", "a", "n"],
        ...                       ["e", "t", "a", "e"],
        ...                       ["i", "h", "k", "r"],
        ...                       ["i", "f", "l", "v"]],
        ...                      ["oath", "pea", "eat", "rain"])
        ["eat", "oath"]

        """

        def _iterate(i_row, i_col, node):
            char = board[i_row][i_col]
            if not char or not node.children[ord(char) - 97]:
                return

            node = node.children[ord(char) - 97]
            if node.word and node.end:
                ret.append(node.word)
                node.end = False

            board[i_row][i_col] = None
            if i_row > 0:
                _iterate(i_row - 1, i_col, node)
            if i_col > 0:
                _iterate(i_row, i_col - 1, node)
            if i_row < len(board) - 1:
                _iterate(i_row + 1, i_col, node)
            if i_col < len(board[0]) - 1:
                _iterate(i_row, i_col + 1, node)
            board[i_row][i_col] = char

        ret = []
        root = self.trie(words)
        for row in range(len(board)):
            for col in range(len(board[0])):
                _iterate(row, col, root)
        return ret
