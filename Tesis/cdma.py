"""
CDMA: encoding decoding in python
Author: manu.datta@gmail.com
"""

from functools import reduce
import itertools
import operator

def mux(codes,data):
    list_data = [list(datum) for datum in data]
    code_map = { index:{1:code,0:map(operator.neg,code)} for index,code in enumerate(codes) }
    mux_input = itertools.zip_longest(*list_data,fillvalue='0')
    def map_data_and_append(data_tick,code_map):
        mapped_codes = [code_map[index][int(bit)] for index,bit in enumerate(data_tick)]
        return reduce(lambda x,a: [x[index]+a[index] for index in range(0,len(a))],mapped_codes)
    encodings = list(itertools.chain.from_iterable((map_data_and_append(tick,code_map) for tick in mux_input)))
    return encodings

def demux(codes,encoded_data):
    code_len = len(codes[0])
    start,end = 0,code_len
    decoded_strs = ['']*code_len
    while end <= len(encoded_data):
        datum = encoded_data[start:end]
        for index in range(0,code_len):
            code = codes[index]
            decoded = sum([x*c for x,c in zip(code,datum)])
            if decoded > 1:
                decoded_strs[index] = decoded_strs[index] + '1'
            else:
                decoded_strs[index] = decoded_strs[index] + '0'
        start,end = end,end+code_len
    return decoded_strs

if __name__ == '__main__':
    codes = [[1, 1, 1, 1], [1, 1, -1, -1], [1, -1, -1, 1], [1, -1, 1, -1]]
    data = ["1101101", "011", "110100010", "00000000000010" ]
    encodings = mux(codes, data)
    print("Encoded data=", encodings)
    print("Decoded data=", demux(codes, encodings))