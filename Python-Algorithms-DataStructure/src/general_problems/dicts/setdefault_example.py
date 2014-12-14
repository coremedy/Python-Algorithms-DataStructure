'''
Created on 2014-12-14

Copyright info: The code here comes, directly or indirectly, from Mari Wahl and her great Python book.
                I'm not the original owner of the code.
                Thanks Mari for her great work!
'''

def usual_dict_insertion(dict_data):
    new_dict = {}
    for k, v in dict_data:
        if k in new_dict:
            new_dict[k].append(v)
        else:
            new_dict[k] = [v]
    return new_dict
            
def set_default_dict_insertion(dict_data):
    new_dict = {}
    for k, v in dict_data:
        new_dict.setdefault(k, []).append(v)
    return new_dict
        
def test_setdef(module_name='this module'):
    dict_data = (('key1', 'value1'),
                ('key1', 'value2'),
                ('key2', 'value3'),
                ('key2', 'value4'),
                ('key2', 'value5'),)
    print(usual_dict_insertion(dict_data))
    print(set_default_dict_insertion(dict_data))
    s = 'Tests in {name} have {con}!'
    print(s.format(name=module_name, con='passed'))

if __name__ == '__main__':
    test_setdef()