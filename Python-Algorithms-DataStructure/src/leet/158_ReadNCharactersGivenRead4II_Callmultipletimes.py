'''
Created on 2015-10-15
'''

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):
def read4(buf):
    pass

class Solution(object):
    def __init__(self):
        self.cache = []
    
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        index = 0
        if len(self.cache) > 0:
            count = min(n, len(self.cache))
            while count > 0:
                buf[index] = self.cache.pop()
                count, index = count - 1, index + 1
            n -= index
        if n > 0:
            n, local_buf = n + index, ['', '', '', '']
            while True:
                chars_read = read4(local_buf)
                actual_chars_needed = min(chars_read, n - index)
                for i in range(0, actual_chars_needed):
                    buf[index + i] = local_buf[i]
                if chars_read > actual_chars_needed:
                    for i in range(chars_read - 1, actual_chars_needed - 1, -1):
                        self.cache.append(local_buf[i])
                index += actual_chars_needed
                if actual_chars_needed < 4:
                    break
        return index

if __name__ == '__main__':
    pass