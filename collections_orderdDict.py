import collections

# Ordered dictionaries are just like regular dictionaries 
# but they remember the order that items were inserted. 
# When iterating over an ordered dictionary, the items 
# are returned in the order their keys were first added.

# If a new entry overwrites an existing entry, 
# the original insertion position is left unchanged. 
# Deleting an entry and reinserting it will move it to the end.

# if it remembers the order the keys were last inserted
# If a new entry overwrites an existing entry, 
# the original insertion position is changed and moved to the end:

# An ordered dictionary can be combined with the Counter class so 
# that the counter remembers the order elements are first encountered:

# .popitem(last=True) -returns and removes a (key, value) pair. 
# The pairs are returned in LIFO order if last is true 
# or FIFO order if false.

# reversed() - for reverse iteration
# will return a iterator with keys in reversed order

# equality btw orderdicts is order sensitive, whereas
# equality btw orderdict and normal dict is not order sensitive

d = {'banana':3, 'apple':4, 'pear':1, 'orange':2}
print(d)
print(collections.OrderedDict(d))
o = collections.OrderedDict(sorted(d.items(),key=lambda x :x[1]))
print(o)