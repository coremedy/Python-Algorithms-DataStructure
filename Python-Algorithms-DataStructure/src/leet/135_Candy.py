'''
Created on 2015-10-27
'''

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        ratings_len = len(ratings)
        if ratings_len <= 1:
            return ratings_len
        base = []
        for index in range(ratings_len):
            if (index == 0 and ratings[index] <= ratings[index + 1]) or (index == ratings_len - 1 and ratings[index - 1] >= ratings[index]) or (ratings[index - 1] >= ratings[index] and ratings[index] <= ratings[index + 1]):
                base.append(index)
        if len(base) == ratings_len:
            return ratings_len
        count = ratings_len
        for i in range(len(base) - 1):
            beg_index, end_index = base[i], base[i + 1]
            if end_index > beg_index + 1: # There is a peak
                peak_beg_index = beg_index + 1
                while peak_beg_index < end_index and ratings[peak_beg_index] < ratings[peak_beg_index + 1]:
                    peak_beg_index += 1 # We got it
                peak_end_index = peak_beg_index + 1
                while peak_end_index < end_index and ratings[peak_beg_index] == ratings[peak_end_index]:
                    peak_end_index += 1    # Peaks with the same value
                count += (0 + peak_beg_index - 1 - beg_index) * (peak_beg_index - beg_index) // 2 + (0 + end_index - peak_end_index) * (end_index - peak_end_index + 1) // 2
                count += max(end_index - peak_end_index + 1, peak_beg_index - beg_index) + min(end_index - peak_end_index + 1, peak_beg_index - beg_index) * (peak_end_index - peak_beg_index - 1)
        if base[0] > 0:
            count += (0 + base[0]) * (base[0] + 1) // 2
        if base[-1] < ratings_len - 1:
            count += (0 + ratings_len - 1 - base[-1]) * (ratings_len - base[-1]) // 2
        return count

if __name__ == '__main__':
    pass