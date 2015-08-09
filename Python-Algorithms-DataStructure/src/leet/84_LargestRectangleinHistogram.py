'''
Created on 2015-08-09
'''

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def largestRectangleArea(self, height):
        if height is None:
            return 0
        if len(height) == 0:
            return 0
        result = [0]
        book_mark = []
        for elem in height:
            if elem == 0:
                self.clean_book_mark(book_mark, result)
            else:
                if len(book_mark) == 0 or elem >= book_mark[-1]:
                    book_mark.append(elem)
                else:
                    self.adjust_book_mark(book_mark, elem, result)
        if len(book_mark) > 0:
            self.clean_book_mark(book_mark, result)
        return result[0]
        
    def adjust_book_mark(self, book_mark, current_val, result):
        book_mark_length = len(book_mark)
        for index in range(book_mark_length - 1, -1, -1):
            if book_mark[index] > current_val:
                result[0] = max(result[0], book_mark[index] * (book_mark_length - index))
                book_mark[index] = current_val
            else:
                break
        book_mark.append(current_val)
        
    def clean_book_mark(self, book_mark, result):
        book_mark_length = len(book_mark)
        if book_mark_length > 0:
            for index in range(book_mark_length):
                result[0] = max(result[0], book_mark[index] * (book_mark_length - index))
            del book_mark[:]

if __name__ == '__main__':
    pass