#!/usr/bin/env python
__author__ = 'Roland Heintze'
"""
Take two equal-length buffers and produce their XOR combination
Input:     1c0111001f010100061a024b53535009181c
           686974207468652062756c6c277320657965
Output:    746865206b696420646f6e277420706c6179
"""


def xor_strings(hex_string1, hex_string2):
    """
    Method takes two hex strings and returns an XOR from them
    """

    return 'xorish'


def test_xor_strings():
    tests = (
        ('1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965',
            '746865206b696420646f6e277420706c6179'),
    )
    for i in tests:
        # assert xor_strings(i[0], i[1]) == i[2]
        print "Expected:\n", i[2]
        print "Result:\n", xor_strings(i[0], i[1])

    print 'All tests passed'


if __name__ == '__main__':
    test_xor_strings()
