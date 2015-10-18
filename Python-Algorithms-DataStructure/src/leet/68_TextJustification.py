'''
Created on 2015-10-18
'''

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if len(words) == 0:
            return [' ' * (maxWidth + 1)]
        if len(words) == 1:
            return [words[0] + ' ' * (maxWidth - len(words[0]))]
        result, buf, buf_len = [], [words[0]], len(words[0])
        for index in range(1, len(words)):
            if buf_len + (0 if len(buf) == 0 or len(buf) == 1 else len(buf) - 1) + 1 + len(words[index]) <= maxWidth:
                buf.append(words[index])
                buf_len += len(words[index])
            else:
                result.append(self.genString(buf, buf_len, maxWidth))
                buf = [words[index]]
                buf_len = len(words[index])
        s = ' '.join(buf)
        result.append(s + ' ' * (maxWidth - len(s)))
        return result

    def genString(self, buf, buf_len, maxWidth):
        if len(buf) == 1:
            return buf[0] + ' ' * (maxWidth - len(buf[0]))
        gap_array, r = [' ' * ((maxWidth - buf_len) // (len(buf) - 1)) for dummy_i in range(len(buf) - 1)], (maxWidth - buf_len) % (len(buf) - 1)
        if r > 0:
            if len(gap_array) == 1:
                gap_array[0] += ' ' * r
            else:
                index = 0
                while r > 0:
                    gap_array[index] += ' '
                    index, r = index + 1, r - 1
        gap_array.append('')
        s = ''
        for index in range(len(buf)):
            s += buf[index] + gap_array[index]
        return s

if __name__ == '__main__':
    pass