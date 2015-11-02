'''
Created on 2015-11-02
'''

class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.d = dict()
        for s in dictionary:
            key = s if len(s) <= 2 else (s[0] + str(len(s) - 2) + s[-1])
            if key not in self.d:
                self.d[key] = set()
            self.d[key].add(s)

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        key = word if len(word) <= 2 else (word[0] + str(len(word) - 2) + word[-1])
        return True if key not in self.d else ((word in self.d[key]) and (len(self.d[key]) == 1))
        
# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")

if __name__ == '__main__':
    pass