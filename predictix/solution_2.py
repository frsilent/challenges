__author__ = 'Roland'
"""
Write a function or sub-routine in your favorite programming language that will read in
an arbitrary English text file as input, parse it into words, and print the count for each
word. For example, if the file contained ‘la tee da tee da’, then the function would print:
la – 1
tee – 2
da – 2
"""


def wordCount(file):
    """
    Takes a file argument, parses it, and displays all words and their frequencies in the format:
    a - 3
    b - 2
    c - 5
    etc
    """

    #create dictionary of all words, key: word, value: frequency
    words = {}
    for item in file.read().split():
        words[item] = words.get(item, 0)+1

    #output data
    for word in words:
        print(word + ' - ' + str(words.get(word)))

if __name__ == '__main__':
    testFile = open('solution_2_test.txt', 'r')
    wordCount(testFile)
