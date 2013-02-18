#Given N terms, your task is to find the k most frequent terms from given N terms.
#Output format :
#Print the k most frequent terms in descending order of their frequency. If two terms have same frequency print them in lexicographical order.

f = open('test_data/ft_input01.txt')
terms = []
for x in range(min(int(f.readline()),300000)):
    terms.append(f.readline().strip())
terms_dict = {}
for item in terms:
    terms_dict[item] = terms_dict.get(item, 0) + 1

#TODO: Need to find a way to sort these so that it's sorted primarily by frequency & then alphabetical
terms = sorted(terms_dict.items(), key=lambda item: item[1], reverse = True)

terms.sort(key=lambda tup: tup[0])

for term in range(int(f.readline())):
    print terms[term][0]