# v7 -- hash = HAS-160

#"дааааа, еб*ть его в рот. втянули меня в какую-ту ху*ню" @я, коли шукав реалізацію has-160

import numpy as np
import scipy as sc
import rhash

#--------------------------------------------------  
#перекодування
def string_to_binary(string):
    res = ''.join(format(i, '08b') for i in bytearray(string, encoding ='utf-8'))
    return res

def binary_to_hex(string):
    res = '%08X' % int(string_to_binary(string), 2)
    return res


def hex_to_binary(string):
    res = str(bin(int(string, base=16)))[2:]
    return res

'''
def binary_to_string(string):
    res = 
    return res
'''
#--------------------------------------------------   




def main():
    credentials = str('Skorobahatko Maksym Ihorovych')
    hash_of_credentials = rhash.hash_msg(credentials, rhash.HAS160)
    print(hash_of_credentials)


if __name__ == '__main__':
    main()