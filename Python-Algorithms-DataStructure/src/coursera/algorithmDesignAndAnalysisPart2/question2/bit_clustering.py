'''
Created on 2015-04-01

Question URL: https://class.coursera.org/algo2-004/quiz/attempt?quiz_id=79
'''

import time

class union_find(object):
    
    def __init__(self, size):
        # Neglect 0 here
        self._pset = [index for index in range(0, size + 1)]
        self._components = size
    
    def findSet(self, vertex):
        if vertex == self._pset[vertex]:
            return vertex
        else:
            # Flatten the tree
            self._pset[vertex] = self.findSet(self._pset[vertex])
            return self._pset[vertex]
    
    def isSameSet(self, vertex_a, vertex_b):
        return self.findSet(vertex_a) == self.findSet(vertex_b)
    
    def unionSet(self, vertex_a, vertex_b):
        root_a = self.findSet(vertex_a)
        root_b = self.findSet(vertex_b)
        if root_a != root_b:
            self._pset[root_a] = root_b
            self._components -= 1
    
    def components(self):
        return self._components

if __name__ == '__main__':
    start_time = time.time()
    bits_table = []
    uf = None
    number_of_bit = 0
    bits_dict = dict()
    # Read input
    with open('C:\\testcases\\clustering_big.txt', 'r') as input_fileHandle:
        count = 1
        for line in input_fileHandle:
            data = line.strip().split()
            if len(data) == 2:
                uf = union_find(int(data[0]))
                number_of_bit = int(data[1])
                for bit_index in range(0, number_of_bit):
                    bits_table.append(1 << bit_index)
            else:
                num = 0
                for bit_index in range(0, number_of_bit):
                    if data[bit_index] == '1':
                        num = num | bits_table[number_of_bit - 1 - bit_index]
                if num not in bits_dict:
                    bits_dict[num] = count
                else:
                    # 0 bit of distance
                    uf.unionSet(bits_dict[num], count)
                count += 1
    # So far so good
    print('Processing input --- %s seconds ---' % (time.time() - start_time))
    start_time = time.time()
    for num_key in bits_dict.keys():
        for outer_index in range(0, number_of_bit):
            num_key_outer = num_key ^ bits_table[outer_index]
            # 1 bit of distance
            if num_key_outer in bits_dict:
                uf.unionSet(bits_dict[num_key_outer], bits_dict[num_key])
            for inner_index in range(outer_index + 1, number_of_bit):
                # Keep num_key_outer untouched in the inner loop
                num_key_inner = num_key_outer ^ bits_table[inner_index]
                # 2 bits of distance
                if num_key_inner in bits_dict:
                    uf.unionSet(bits_dict[num_key_inner], bits_dict[num_key])
    print('Generating Clusters --- %s seconds ---' % (time.time() - start_time))
    print(uf.components())