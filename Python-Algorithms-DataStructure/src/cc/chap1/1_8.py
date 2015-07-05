'''
Created on 2015-07-05

Question: Assume you have a method isSubstring which checks if one word is a substring of another.
          Given two strings, s1 and s2, write code to check if s2 is a rotation if s1 using only one call to isSubstring
'''

def check_rotation(s2, s1):
    if len(s1) > 0:
        if len(s2) == len(s1): 
            # isSubstring
            return (s2 in (s1 + s1))
    return False

if __name__ == '__main__':
    print(check_rotation('pperJackTheRi', 'JackTheRipper'))