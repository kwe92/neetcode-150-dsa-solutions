class TrieNode():
    def __init__(self):
        self.children = {}
        self.endOfString = False

    def __repr__(self):
        return f'TrieNode(children: {self.children}, endOfString: {self.endOfString})'


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfString = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.endOfString

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True


if __name__ == '__main__':
    pTree = PrefixTree()
    pTree.insert('apple')
    pTree.insert('ape')
    print(pTree.search('apple'))
    print(pTree.startsWith('app'))
    # print(f'root: {pTree.root}')
