'''
Created on 2015-07-28
'''

class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.siblings = dict()
        self.inclusive = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        current = self.root
        for index in range(len(word)):
            if word[index] not in current.siblings:
                current.siblings[word[index]] = TrieNode()
            current = current.siblings[word[index]]
        current.inclusive = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        current = self.root
        for index in range(len(word)):
            if word[index] not in current.siblings:
                return False
            current = current.siblings[word[index]]
        return current.inclusive

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        current = self.root
        for index in range(len(prefix)):
            if prefix[index] not in current.siblings:
                return False
            current = current.siblings[prefix[index]]
        return True

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")

if __name__ == '__main__':
    pass