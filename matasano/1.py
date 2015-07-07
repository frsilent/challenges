#!/usr/bin/env python
__author__ = 'Roland Heintze'
"""
Convert hex to base64
Input:     49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
Output:    SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
"""


def base64(hex_string):
    """
    Method takes a hex string & returns a base64 conversion of it
    (base64 meaning the numbering system has 64 different digits)
    """
    import binascii
    binary = binascii.unhexlify(hex_string)
    return binascii.b2a_base64(binary)


def test_base64():
    tests = (
        ('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d',
            'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'),
    )
    for i in tests:
        assert base64(i[0]) == i[1]
        print "Expected:\n", i[1]
        print "Result:\n", base64(i[0])

    print 'All tests passed'


if __name__ == '__main__':
    test_base64()
