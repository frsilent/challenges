class Buffer:
    """Circular buffer class. Allows users to append, remove and list the contents."""


    def __init__(self, size):
        """
        The new items are appended to the end and the order is retained i.e elements are placed in increasing order
        of their insertion time. When the number of elements in the list elements exceeds the defined size,
        the older elements are overwritten.
        """
        self.size = max(0,min(size,10000)) #0 <= N <= 10000
        self.data = []
        self.head = 0
        self.tail = 0
        full = False

    def append(self,x):
        """
        Append the following n lines to the buffer. If the buffer is full they replace the older entries.
        """
        if len(self.data) > self.size:
            self.full = True
            self.data[self.head] = x
            self.head += 1
        else:
            self.data.append(x)
            self.tail += 1

    def remove(self, x):
        """
        Remove first n elements of the buffer. These n elements are the ones that were added earliest among the
#       current elements.
        """
        for item in range(x):
            del self.data[item]
            self.head+=1

    def get(self):
        """
        #"L"   - List the elements of buffer in order of their inserting time.
        """
        for item in self.data:
            print item

f = open('test_data/cb_input00.txt')
testingBuffer = Buffer(int(f.readline()))

while True:
    selection = f.readline()
    if selection[0] == 'A':
        for items in range(int(selection[2:])):
            testingBuffer.append(f.readline())
    elif selection[0] == 'R':
        testingBuffer.remove(int(selection[2:]))
    elif selection[0] == 'L':
        print testingBuffer.get()
    elif selection[0] == 'Q':
        break
    else:
        print 'Invalid option'