import sys
import numpy as np
from array import *

utf8_1byte = '0xxxxxxx'
utf8_2bytes = '110xxxxx 10xxxxxx'
utf8_3bytes = '1110xxxx 10xxxxxx 10xxxxxx'
utf8_4bytes = '11110xxx 10xxxxxx 10xxxxxx 10xxxxxx'


def encode_utf8(input_filename, output_filename):
    """
    :param input_filename: the input file name (encoded in utf-16)
    :param output_filename: the output file name (encoded in utf-8)
    function converts encoding to utf-8
    assumption : it contains characters from Unicode's Basic Multilingual Plane (U+0000 to U+FFFF) in UTF-16 encoding,
    i.e., every 2 bytes correspond to one character and encodes that character's Unicode code point, in big endian.
    Ref : https://tools.ietf.org/html/rfc3629#page-4
    """
    file_reader = open(input_filename, 'rb')
    file_writer = open(output_filename, 'wb')

    with file_reader as f:
        while 1:
            bytes2 = f.read(2)
            if not bytes2:
                break

            utf8_binary = ''
            if bytes2[0] == int('0',16) and bytes2[1] <= int('7f', 16):
                binary = copy_bits(bytes2, 7)
                utf8_binary = replace_x(utf8_1byte, binary)
            elif int('0', 16) <= bytes2[0] <= int('07', 16) and int('80', 16) <= bytes2[1] <= int('ff', 16):
                binary = copy_bits(bytes2, 11)
                utf8_binary = replace_x(utf8_2bytes, binary)
            elif int('08', 16) <= bytes2[0] <= int('ff', 16):
                binary = copy_bits(bytes2, 16)
                utf8_binary = replace_x(utf8_3bytes, binary)
            else:
                print('********************ERROR********************')

            utf8_binary = utf8_binary.replace(' ', '')
            write_binary_string_file(file_writer, utf8_binary)

    file_reader.close()
    file_writer.close()


def copy_bits(bytes2, num_of_bits):
    """
    return num_of_bits bits starting from lower order bits in bytes2, which has 2 bytes
    """
    bitstring = ''
    current_byte = bytes2[1]
    for i in range(num_of_bits):
        if i == 8:
            current_byte = bytes2[0]
            
        bitstring += str(current_byte & 1)
        current_byte >>= 1
    return ''.join(reversed(bitstring))


def replace_x(template, bits):
    """
    replaces x in the template with bits, starting from least significant bits
    """
    binary = template
    for i in range(len(bits)):
        k = binary.rfind('x')
        current_bit = bits[len(bits) - 1 - i]
        binary = binary[:k] + current_bit + binary[k + 1:]
    return binary


def write_binary_string_file(file_writer, b):
    """
    replaces x in the template with bits, starting from least significant bits
    """
    bin_array = array('B')
    i = 0
    for i in range(int(len(b) / 8)):
        b_byte = int(b[(i * 8):(i + 1) * 8], 2)
        # print(b_byte, b[(i * 8):(i+1) * 8])
        bin_array.append(b_byte)
        # print(b_byte)
        i += 1

    final_bin_array = array('B')
    final_bin_array.extend(list(reversed(bin_array)))
    bin_array.tofile(file_writer)


encode_utf8('japanese_in.txt', 'japanese_out.txt')
#encode_utf8('english_in.txt', 'english_out.txt')

'''
file_reader = open('english_out.txt', 'rb')

with file_reader as f:
    while 1:
        bytes2 = f.read(1)
        if not bytes2:
            break
        print(bytes2[0])
'''
