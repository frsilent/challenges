#TODO: I hope this is accurate. It was actually pretty easy.
f = open('test_data/mul_input00.txt')
count = int(f.readline())

elements = []
for item in range(count):
    elements.append(int(f.readline().strip()))

output = []
list_product = reduce(lambda x, y: x * y, elements) #finds a number as a multiple of all list elements
for new_element in range(count-1):
    output.append(list_product /  elements[new_element])
print output