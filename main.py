# v7 -- hash = HAS-160

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

h = rhash.HAS160

def hash_function(string):
    string = string_to_binary(string)
    
    h0 = '00000000'
    h1 = '67452301'
    h2 = 'EFCDAB89'
    h3 = '98BADCFE'
    h4 = '10325476'
    
    ml = len(string)
    
    


def main():
    return 

if __name__ == '__main__':
    main()