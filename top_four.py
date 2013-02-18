f = open('test_data/tf_input01.txt')
count = f.readline()
terms = []
for i in range(int(count)):
    terms.append(int(f.readline().strip()))
terms.sort(reverse=True)
for i in range(4):
    print(terms[i])