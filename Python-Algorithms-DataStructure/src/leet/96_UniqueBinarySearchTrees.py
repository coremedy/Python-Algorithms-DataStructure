'''
Created on 2015-07-18

NUM[0] - Empty tree  - 1
NUM[1] - Single node - 1 (the value of the node does not matter!)
NUM[2] - Two node    - 2 (the values of nodes do not matter!)

GROUP 1                 GROUP 2                  GROUP 3

  1        1                   2                      3            3
   \        \                /  \                    /            / 
    3        2              1    3                 2             1
   /          \                                   /               \
 2             3                                 1                 2
 
LEFT  SUBTREE NUM[0]    LEFT  SUBTREE NUM[1]     LEFT  SUBTREE NUM[2]
RIGHT SUBTREE NUM[2]    RIGHT SUBTREE NUM[1]     RIGHT SUBTREE NUM[0]
NUM[0] * NUM[2]         NUM[1] * NUM[1]          NUM[2] * NUM[0]
                        Why? How many ways to
                        generate a BST with
                        only node 1? NUM[1]!
                        How many ways to
                        generate a BST with
                        only node 3? NUM[1]!

NUM[3] = NUM[0] * NUM[2] + NUM[1] * NUM[1] + NUM[2] * NUM[0]
'''

class Solution:
    # @param {integer} n
    # @return {integer}
    def numTrees(self, n):
        if n == 1:
            return 1
        else:
            NUM = [ 1 for dummy_index in range(0, n + 1)]
            for index in range(2, n + 1):
                NUM[index] = 0
                for inner_index in range(0, index):
                    NUM[index] += NUM[inner_index] * NUM[index - 1 - inner_index]
            return NUM[n]

if __name__ == '__main__':
    pass