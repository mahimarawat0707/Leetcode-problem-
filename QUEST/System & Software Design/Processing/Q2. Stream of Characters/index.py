from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        self.stream = []

        # Insert reversed words into Trie
        for word in words:
            node = self.root
            for ch in reversed(word):
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.end = True

    def query(self, letter: str) -> bool:
        self.stream.append(letter)

        node = self.root
        # Traverse stream backwards
        for ch in reversed(self.stream):
            if ch not in node.children:
                return False
            node = node.children[ch]
            if node.end:
                return True

        return False
