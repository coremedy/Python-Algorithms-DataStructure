'''
Created on 2015-10-13
'''

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1_table, version2_table = [int(ch1) for ch1 in version1.split('.')], [int(ch2) for ch2 in version2.split('.')]
        for index in range(min(len(version1_table), len(version2_table))):
            if version1_table[index] > version2_table[index]:
                return 1
            elif version1_table[index] < version2_table[index]:
                return -1
        if len(version1_table) == len(version2_table):
            return 0
        if len(version1_table) > len(version2_table) and sum(version1_table[len(version2_table):]) > 0:
            return 1
        if len(version1_table) < len(version2_table) and sum(version2_table[len(version1_table):]) > 0:
            return -1
        return 0

if __name__ == '__main__':
    pass