'''
Created on 2015-10-16
'''

class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        buffer = []
        for s in strs:
            buffer.append(str(len(s)) + '#' + s)
        return ''.join(buffer)

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        if s == '':
            return []
        strs, start, current = [], 0, 0
        while True:
            if s[current] == '#':
                count = int(s[start : current])
                strs.append('' if count == 0 else s[current + 1 : current + count + 1])
                start = current = current + count + 1
                if start == len(s):
                    break
            else:
                current += 1
        return strs

if __name__ == '__main__':
    pass