'''
Created on 2015-07-31
'''

class Solution:
    # @param {string} beginWord
    # @param {string} endWord
    # @param {set<string>} wordDict
    # @return {integer}
    def ladderLength(self, start, end, Dict):
        characters = 'abcdefghijklmnopqrstuvwxyz'
        phase_table = [{end : set()}]
        phase_index = 1
        successful = False
        while True:
            current_phase_dict = dict()
            for word in phase_table[phase_index - 1].keys():
                for index in range(len(word)):
                    # There are more words than characters !
                    for character_index in range(26):
                        if characters[character_index] != word[index]:
                            new_word = word[:index] + characters[character_index] + word[index + 1:]
                            if new_word == start or new_word in Dict:
                                if new_word not in current_phase_dict:
                                    current_phase_dict[new_word] = set([word])
                                else:
                                    current_phase_dict[new_word].add(word)
                                if new_word == start:
                                    successful = True
            if len(current_phase_dict) == 0:
                break
            phase_table.append(current_phase_dict)
            # Key of BFS - eliminate cycles
            Dict = Dict - set(current_phase_dict.keys())
            phase_index += 1
            if successful == True:
                break
        if not successful:
            return 0
        return phase_index

if __name__ == '__main__':
    pass