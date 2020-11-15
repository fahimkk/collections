import collections

d = {'red':3,'blue':2}
#print(d['green']) # will raise key error
def def_value():
    return 'Not present'

dd = collections.defaultdict(def_value,d)
# we can pass dict as 2nd argument
# we can also pass lambda fuction
# instead of a fuction we can use list,set,int, etc
# list return empy list, int return 0, etx
dd['yello'] = 2
#print(dd)
#print(dd['green']) # will print not present

# missing
# if we want to return the default function value
# for the existing key in the dict
dd.__missing__('red')
#print(dd['red']) # or
#print(dd.__missing__('red'))

# usage of list as a default_factory
s = [('yellow',1),('blue',3),('yellow',2),('blue',4),('red',8)]
sd = collections.defaultdict(list)
for k,v in s:
    sd[k].append(v)
#print(sd)
#print(sd.items())

# normal dict method
normal_dict = {}
for k,v in s:
    normal_dict.setdefault(k,[]).append(v)
#print(normal_dict)

# int as a default_factory
s_int = 'mississippi'
sd_int = collections.defaultdict(int)
for w in s_int:
    sd_int[w]+=1
#print(sd_int)
# if we need a constant value rather than zero,
# we can use itertools.repeat() method, which take 
# the value as argument, and no of times to repeat,
# 2nd argument is optional, otherwise it is infinity.

# set as a default factory
set_dict = collections.defaultdict(set)
for k,v in s:
    set_dict[k].add(v)
print(set_dict)