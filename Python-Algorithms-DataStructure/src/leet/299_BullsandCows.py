'''
Created on 2015-11-05
'''

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull, cow, sec_dict, gue_dict = 0, 0, dict(), dict()
        for index in range(len(secret)):
            if secret[index] == guess[index]:
                bull += 1
            else:
                if secret[index] not in sec_dict:
                    sec_dict[secret[index]] = 0
                sec_dict[secret[index]] += 1
                if guess[index] not in gue_dict:
                    gue_dict[guess[index]] = 0
                gue_dict[guess[index]] += 1
        for k in gue_dict:
            if k in sec_dict:
                cow += min(gue_dict[k], sec_dict[k])
        return str(bull) + 'A' + str(cow) + 'B'

if __name__ == '__main__':
    pass