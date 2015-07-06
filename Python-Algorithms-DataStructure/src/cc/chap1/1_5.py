'''
Created on 2015-07-06

Question: Implement a method to perform basic string compression using the counts of repeated characters.
          For example, the string aabcccccaaa would become a2b1c5a3.
          If the "compressed" string would not become smaller than the original string, you method should return the original string,
'''

def compress(source_str):
    if source_str is None:
        return source_str
    if len(source_str) == 0:
        return source_str
    byte_array = bytearray()
    count = 1
    current = ord(source_str[0])    
    for index in range(1, len(source_str)):
        if current == ord(source_str[index]):
            count += 1
        else:
            byte_array.append(current)
            byte_array.append(count + 48)
            count = 1
            current = ord(source_str[index])
    # Do not forget the following two lines 
    byte_array.append(current)
    byte_array.append(count + 48)    
    if len(source_str) < len(byte_array):
        return source_str
    else:
        return byte_array.decode('ascii')

if __name__ == '__main__':
    print(compress('aabcccccaaa'))