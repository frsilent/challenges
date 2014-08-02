class Buffer:
    """Circular buffer class. Allows users to append, remove and list the contents."""

    def __init__(self, size):
        """
        The new items are appended to the end and the order is retained i.e elements are placed in increasing order
        of their insertion time. When the number of elements in the list elements exceeds the defined size,
        the older elements are overwritten.
        """
        self.size = max(0, min(size, 10000))  # 0 <= N <= 10000
        self.data = []
        self.head = 0  # index to the oldest element
        self.tail = 0  # index to the newest element
        full = False

    def append(self, x):
        """
        Append the following n lines to the buffer. If the buffer is full they replace the older entries.
        """
        if len(self.data) > self.size:
            self.full = True
            self.data[self.head] = x
            self.head += 1
            self.tail += 1
        else:
            self.data.append(x)
            self.tail += 1

    def remove(self, n):  # TODO: Fix this
        """
        Remove first n elements of the buffer. These n elements are the ones that were added earliest among the
#       current elements.
        """
        for item in range(n):
            del self.data[self.head]
            self.head += 1

    def get(self):
        """
        #"L"   - List the elements of buffer in order of their inserting time.
        """
        # TODO: Make this print out in order of insertion time, so start from head & end at tail
        for item in self.data:
            print item

f = open('test_data/cb_input00.txt')
testingBuffer = Buffer(int(f.readline()))

while True:
    selection = f.readline()
    print 'Present buffer: '
    testingBuffer.get()
    if selection[0] == 'A':
        for item in range(int(selection[2:])):  # calls append for the number of lines specified
            testingBuffer.append(f.readline())
    elif selection[0] == 'R':
        # calls remove for elements specified
        print 'calling remove ' + selection[2:]
        testingBuffer.remove(int(selection[2:]))
    elif selection[0] == 'L':
        print testingBuffer.get()
    elif selection[0] == 'Q':
        break
    else:
        print 'Invalid option'
