class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfword = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfword = True

    def search(self, word: str) -> bool:
        def dfs(j: int, node: TrieNode) -> None:
            curr = node
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.endOfword
        return dfs(0, self.root)


if __name__ == '__main__':
    wordDictionary = WordDictionary()
    wordDictionary.addWord("day")
    wordDictionary.addWord("bay")
    wordDictionary.addWord("may")
    print(wordDictionary.search("say"))  # return false
    print(wordDictionary.search("day"))  # return true
    print(wordDictionary.search(".ay"))  # return true
    print(wordDictionary.search("b.."))  # return true
