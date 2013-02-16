#There are four types of commands.
# 
#"A"  n -  Append the following n lines to the buffer. If the buffer is full they replace the older entries.
#"R"  n -  Remove first n elements of the buffer. These n elements are the ones that were added earliest among the
#          current elements.
#"L"   - List the elements of buffer in order of their inserting time.
#"Q"  - Quit.  
# 
#Your task is to execute commands on circular buffer.
# 
#Input format :
# 
#First line of input contains N ,  the size of the buffer.
#A n  - append the following n lines to the buffer.
#R n - remove first n elements of the buffer.
#L - list the buffer.
#Q - Quit.
# 
#Output format :
# 
# Whenever  L command appears in the input, print the elements of buffer in order of their inserting time. Element
# that was added first should appear first.
# 
#Sample Input :
# 
#10
#A 3
#Fee
#Fi
#Fo
#A 1
#Fum
#R 2
#L
#Q
# 
#Sample Output :
# 
#Fo
#Fum

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
        Adds to the buffer
        If the buffer is full, the oldest elements are overwritten (the head)
        """
        if len(self.data) > self.size:
            self.full = True
            self.data[self.head] = x
            self.head += 1
        else:
            self.data.append(x)
            self.tail += 1

    def remove(self, removal_index):
        """
        Removes an element from the buffer
        """
        self.get(removal_index)

    def get(self):
        return self.data



f = open('/home/frsilent/git/challenges/test_data/cb_input00.txt')
testingBuffer = Buffer(int(f.readline()))

selection = f.readline()
while selection[0] != 'Q':
    if selection[0] == 'A':
        for items in range(int(selection[2])):
            testingBuffer.append(f.readline())
    elif selection[0] == 'R':
        pass
    elif selection[0] == 'L':
        pass
    else:
        print 'Invalid option'
        break