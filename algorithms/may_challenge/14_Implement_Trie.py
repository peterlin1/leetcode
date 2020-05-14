class TrieNode:

    def __init__(self):
        self.children = {}
        self.end = False


class Trie(object):
    """
    Implement a trie with insert, search, and startsWith methods.

    Note:
    You may assume that all inputs are consist of lowercase letters a-z.
    All inputs are guaranteed to be non-empty strings.

    15 / 15 test cases passed.
    Status: Accepted
    Runtime: 196 ms
    Memory Usage: 31.2 MB

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
            if not _root.children.get(word[level]):
                _root.children[word[level]] = TrieNode()
            _root = _root.children[word[level]]
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
            try:
                _root = _root.children[word[level]]
            except KeyError:
                return False
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
            try:
                _root = _root.children[prefix[level]]
            except KeyError:
                return False
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
