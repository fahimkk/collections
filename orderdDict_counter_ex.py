import collections
f = open('text.txt','r').read()
count_dict = collections.Counter()
for word in f:
    count_dict[word] +=1
print('Count Dict: ',count_dict)
print('Most Common 5 words:',count_dict.most_common(5))
print('Least Common 5 words: ',count_dict.most_common()[:-5:-1]) # least common

# to sort words from heigh to low 
orderd_dict = collections.OrderedDict(sorted(count_dict.items(),\
                    key=lambda x: x[1], reverse=True))
print('Sorted Dict: ', orderd_dict)
