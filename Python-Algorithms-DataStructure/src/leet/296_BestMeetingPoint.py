'''
Created on 2015-10-27
'''

class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_count, col_count = len(grid), len(grid[0])
        x_array, y_array = [0] * col_count, [0] * row_count
        for r in range(row_count):
            for c in range(col_count):
                if grid[r][c] == 1:
                    y_array[r] += 1
                    x_array[c] += 1
        return self.calculate(x_array) + self.calculate(y_array)

    def calculate(self, array):
        baseline, right = sum([(index * array[index]) if array[index] > 0 else 0 for index in range(len(array))]), sum(array)
        min_val, left, right = baseline, array[0] if array[0] > 0 else 0, (right - array[0]) if array[0] > 0 else right
        for index in range(1, len(array)):
            baseline = baseline + left - right
            min_val = min(min_val, baseline)
            if array[index] > 0:
                left, right = left + array[index], right - array[index]
        return min_val

if __name__ == '__main__':
    pass