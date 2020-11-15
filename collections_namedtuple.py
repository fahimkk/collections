
import collections

# a namedtuple is a regular python class

p_namedtuple = collections.namedtuple('Point',['x','y'])
# we can assign value as list or in a sigle string 
p = p_namedtuple(11,12)
# we can assign as x=11, y=12
#print(p_namedtuple)
#print(p)
#print(p[0])
#print(p.x)
#print(getattr(p,'x'))

# _make method, to make a list into namedtuple instance
# ie we have to pass an iterable object
t = [35,86]
q = p_namedtuple._make(t)
#print(q)

# ** to convert a dict to namedtuple
dictionary = {'x':1,'y':2}
d = p_namedtuple(**dictionary)
#print(d)

import csv
EmplyoeeRecord = collections.namedtuple('EmployeeRecord',\
                'name, age, department, place')
#for emp in map(EmplyoeeRecord._make, csv.reader(\
#                    open('collection_namedtuple.csv','r'))):
#    print(emp.name, emp.place)

# _asdict() return a new orderdDict
p_orderdDict = p._asdict()
#print(p)
#print(p_orderdDict)

# _replace() returns a NEW instance with replacing specified field value
#print(p)
p_replaced = p._replace(x=33)
#print(p)
#print(p_replaced)

# _fields
#print(p_namedtuple._fields)
#print(EmplyoeeRecord._fields)
Color = collections.namedtuple('Color','red green blue')
Pixel = collections.namedtuple('Pixel',p_namedtuple._fields+Color._fields)
#print(Pixel._fields)
p_pixel = Pixel(11,22,128,256,0)
#print(p_pixel)

# Enumerated constants can be implemented with named tuples, 
# but it is simpler and more efficient to use a simple class declaration:
Status = collections.namedtuple('Status','opens pending close')._make(range(3))
#print(Status.opens, Status.pending, Status.close)
class Status_1:
    opens, pending, close = range(3)
#print(Status_1.opens, Status_1.pending, Status_1.close)