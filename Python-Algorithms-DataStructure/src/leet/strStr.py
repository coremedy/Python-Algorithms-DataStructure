'''
Created on 2015-02-01
'''

class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        # haystack is None
        if haystack is None:
            return -1
        # haystack not None
        else:
            # haystack is empty string
            if len(haystack) == 0:
                # needle is None
                if needle is None:
                    return -1
                else:
                    # needle is empty string
                    if len(needle) == 0:
                        return 0
                    else:
                        return -1
            # haystack is normal string
            else:
                # needle is None
                if needle is None:
                    return -1
                else:
                    # needle is empty string
                    if len(needle) == 0:
                        return 0
                    # KMP
                    else:
                        i, j = 0, 0
                        nextTable = self.__genNext(needle)
                        len_haystack = len(haystack)
                        len_needle = len(needle)
                        while (i < len_haystack) and (j < len_needle):
                            if (j == -1) or (haystack[i] == needle[j]):
                                i += 1
                                j += 1
                            else:
                                j = nextTable[j]
                        if j == len_needle:
                            return i - j
                        else:
                            return -1

    def __genNext(self, needle):
        len_needle = len(needle)
        nextTable = [i - i for i in range(0, len_needle)]
        nextTable[0] = -1
        k, j = -1, 0
        while j < len_needle - 1:
            if (k == -1) or (needle[k] == needle[j]):
                k += 1
                j += 1
                nextTable[j] = k
            else:
                k = nextTable[k]            
        return nextTable

if __name__ == '__main__':
    s = Solution()
    print(s.strStr('', ''))