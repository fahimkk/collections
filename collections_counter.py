import collections

# counter is a dict with element as key
# and its count as value

l1 = [2,1,2,2,4,5,3,4,3,2]
cnt_list = collections.Counter(l1)
# we can pass a string also 
#print(cnt_list)

d1 = {'red':3, 'blue':1}
d2 = {'red':'color','car':'vehicle'}
# in d2 return the same dict, and for 
# most_common it consider the len(value)
cnt_dict = collections.Counter(d1)
#print(cnt_dict)
#print(cnt_dict['green']) # for missing element returns zero

# we can assign by using equal sign, dont need quotation for string
cnt = collections.Counter(cat=4,dog=5)
#print(cnt)

word_count = collections.Counter()
f=open('threading_mydata.txt').read()
for word in f:
    word_count[word] +=1
# by normal dict
word_count_normaldict = {}
for word in f:
    word_count_normaldict[word] = word_count_normaldict.get(word,0)+1
#print(word_count == word_count_normaldict)

# to get most common words 
#print(word_count.most_common(5))

# to get least common, use -ve befor number
#print(word_count.most_common()[:-5:-1])
# [::1] for high to low, [::-1] for reverse

# to get the elements
c = collections.Counter(a=4, b=2, c=0, d=-2)
#print(c.keys()) # only return unique elements
# elements will return all the keys wrt count
# returns an iterator, convert it into list
#print(list(c.elements()))

# update and fromkeys methods won't work in counter
x= ('key1','key2','key3')
# x can be any hashable object like list,string,set,dict etc
y=1
# for each in x, place whole y as value
# if y is not given it set None as value
d2 = dict.fromkeys(x,y)
#print(d2)
# update take a dict as argument like extend 
d2.update({'key4':2})
#print(d2)

# subtract
c = collections.Counter(a=4, b=2, c=0, d=-2)
d = collections.Counter(a=1, b=2, c=3, d=4)
#c.subtract(d)
#c.clear() # to clear the dict
#print(c)
#print(c+d)
#print(c-d)
#print(c&d)
#print(c|d)