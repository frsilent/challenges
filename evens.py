__author__ = 'Roland Heintze'
"""
Given an array of integer values, return all even numbers.
Constraints:
    1. Cannot iterate over the array
    2. Cannot use map/filter/reduce
"""


def evens(integerList, results=None):
    """
    Recursive method returns even numbers from an array
    """

    if results is None:
        results = []

    if len(integerList) == 1:
        if integerList[0] % 2 == 0:
            results.append(integerList[0])
    else:
        if integerList[0] % 2 == 0:
            results.append(integerList[0])
        evens(integerList[1:], results)
    return results


if __name__ == '__main__':
    tests = (
        ([-10, 2, 3, -2, 5, -15], [-10, 2, -2]),
        ([0], [0]),
        ([1], []),
        ([-1], []),
        ([-2], [-2]),
        ([2], [2]),
        ((0, 2), [0, 2]),  # testing against tuples
    )

    for i in tests:
        assert evens(i[0]) == i[1]
        print "Expected:\n", i[1]
        print "Result:\n", evens(i[0])

    print 'All tests passed'
