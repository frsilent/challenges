__author__ = 'Roland'
""" Write a function or sub-routine in your favorite programming language which, when
given a list of integers will return the largest sum of contiguous integers in the list. For
example, if the input is (-10, 2, 3, -2, 5, -15), the function will return 8.
"""


def contiguousSum(integerList):
    """
    Receives a list of integers and returns the largest possible sum which can be generated by a contiguous splice.
    ie -2,3,4,5 = 3+4+5 , -10,2,3,-2,5,-15 = 2+3+(-2)+5
    """

    #(Kadane's Algorithm solution http://en.wikipedia.org/wiki/Maximum_subarray_problem)
    # currentMax = lastMax = 0
    # for i in integerList:
    #     currentMax = max(0, currentMax + i)
    #     lastMax = max(lastMax, currentMax)
    # return currentMax

    #Brute force to get all contiguous subarrays
    subarrays = [integerList[i:j] for i in range(0, len(integerList)) for j in range(i + 1, len(integerList) + 1)]

    #Create a list associated by sum() to subarrays
    subSums = [sum(i) for i in subarrays]

    return max(subSums)  # returns the largest sum of the subarrays

if __name__ == '__main__':
    #testing
    assert contiguousSum([-10, 2, 3, -2, 5, -15]) == 8
    assert contiguousSum([1]) == 1
    assert contiguousSum([-1]) == -1
    assert contiguousSum((0, 2)) == 2  # works for tuples too =D
