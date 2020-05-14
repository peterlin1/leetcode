class TrieNode:

    def __init__(self):
        self.children = [None] * 26
        self.end = False


class Trie(object):
    """
    Implement a trie with insert, search, and startsWith methods.

    Note:
    You may assume that all inputs are consist of lowercase letters a-z.
    All inputs are guaranteed to be non-empty strings.

    Runtime: 228 ms, faster than 32.58% of Python3 online submissions for Implement Trie (Prefix Tree).
    Memory Usage: 33 MB, less than 7.41% of Python3 online submissions for Implement Trie (Prefix Tree).

    """

    def __init__(self):
        """
        Initialize your data structure here.

        """

        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.

        Parameters
        ----------
        word : str

        """

        _root = self.root
        for level in range(len(word)):
            # int value of 'a'
            idx = (ord(word[level]) - 97)
            if not _root.children[idx]:
                _root.children[idx] = TrieNode()
            _root = _root.children[idx]
        _root.end = True

    def search(self, word):
        """
        Returns if the word is in the trie.


        Parameters
        ----------
        word : str


        Returns
        -------
        ret : bool

        """

        _root = self.root
        for level in range(len(word)):
            # int value of 'a'
            idx = (ord(word[level]) - 97)
            if not _root.children[idx]:
                return False
            _root = _root.children[idx]
        return True if _root.end is True else False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.


        Parameters
        ----------
        prefix : str


        Returns
        -------
        ret : bool

        """

        _root = self.root
        for level in range(len(prefix)):
            # int value of 'a'
            idx = (ord(prefix[level]) - 97)
            if not _root.children[idx]:
                return False
            _root = _root.children[idx]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
if __name__ == "__main__":
    ex1 = Trie()
    ex1.insert("apple")

    #  returns true
    ex1.search("apple")
    # returns false
    ex1.search("app")
    # returns true
    ex1.startsWith("app")
    ex1.insert("app")
    # returns true
    ex1.search("app")
