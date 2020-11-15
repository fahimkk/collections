import collections
import csv

Toyota = collections.namedtuple('Toyota','Model Year BS CC ')

old_data = csv.reader(open('toyota_old.csv','r')) #a generator
new_data = csv.writer(open('toyota_new,csv','w'))
# _make method used to convert a list into a namedtuple
for toyota in map(Toyota._make,old_data):
    # replace will maintain the rest of the data as the same
    updated = toyota._replace(BS = 'BS-VI',Year=2020)
    new_data.writerow(updated)


