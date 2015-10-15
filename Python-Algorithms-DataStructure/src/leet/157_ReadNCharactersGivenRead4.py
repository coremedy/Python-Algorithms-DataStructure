'''
Created on 2015-10-15
'''

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
def read4(buf):
    pass

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        if n <= 0:
            return 0
        char_read, local_buffer, local_count = 0, ['', '', '', ''], 4
        while local_count == 4 and char_read < n:
            local_count = min(read4(local_buffer), n - char_read)
            for i in range(local_count):
                buf[char_read + i] = local_buffer[i]
            char_read += local_count
        return char_read

if __name__ == '__main__':
    pass