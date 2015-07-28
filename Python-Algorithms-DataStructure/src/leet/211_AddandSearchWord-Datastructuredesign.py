'''
Created on 2015-07-28
'''

class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.siblings = dict()
        self.inclusive = False

class WordDictionary:
    # initialize your data structure here.
    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        current = self.root
        for index in range(len(word)):
            if word[index] not in current.siblings:
                current.siblings[word[index]] = TrieNode()
            current = current.siblings[word[index]]
        current.inclusive = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        return self.searchRecusive(word, self.root)
    
    def searchRecusive(self, word, current):
        if len(word) == 0:
            return current.inclusive
        if word[0] == '.':
            for k in current.siblings.keys():
                if self.searchRecusive(word[1:], current.siblings[k]):
                    return True
            return False
        else:
            if word[0] in current.siblings:
                return self.searchRecusive(word[1:], current.siblings[word[0]])
            return False

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")

if __name__ == '__main__':
    pass