import collections

# append(x), appendleft(x), clear(), count(x), extend(iterable), 
# pop(), popleft(), remove(value), reverse() 

# extendleft(iterable) reverse the x
a = collections.deque(['a','b','c'])
b = [1,2,3,4,5]
a.extendleft(b)
#print(a)

# rotate, n = +ve rotate right, =-ve rotate left
r = collections.deque(['a','b','c','d','e'])
r.rotate(2)
r.rotate(-2)
#print(r)

# reverse return None, reversed returns a deque
b = collections.deque(b)
c = collections.deque(reversed(b))
#print(c)

# to get a deque of last n elements in a deque 
#print(collections.deque(b,2))

# slicing using rotate method
# normal slice doesn't work for deque
d = collections.deque([0,1,2,3,4,5,6,7,8,9])
def deque_slice(deque,m,n):
    """form m to n, not including n
    both m & n are +ve """
    import copy
    deque_copy = copy.deepcopy(deque) 
    deque_copy.rotate(n)
    for _ in range(m+n):
        deque_copy.popleft()
    return deque_copy
#print(d)
#print(deque_slice(d,2,5))
#print(d)

# delete method
#del d[index]
def my_delete(deque,index):
    deque.rotate(-index)
    deque.popleft()
    deque.rotate(index)
my_delete(d,2)
print(d)

def moving_average(iterable, n=3):
    """ moving_average([40, 30, 50, 46, 39, 44]) 
        --> 40.0 42.0 45.0 43.0 """
    import itertools
    it = iter(iterable)
    # create a deque with 2 elements and pop it from it
    d = collections.deque(itertools.islice(it,n-1))
    # appendleft(0) for removing first one every cycle
    d.appendleft(0)
    s = sum(d)
    for element in it:
        # element is next element which is not in d
        # poped the first element from d, and 
        # add the diff to sum
        s += element - d.popleft()
        d.append(element)
        yield s/float(n)
x = [40,30,50,46,39,44]
print(list(moving_average(x,n=3)))

