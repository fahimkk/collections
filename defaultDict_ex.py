import collections
# example of defaultdict 
def dict_reverse(adj):
    """ acyclic directional graph
        key : vertex
        value: a dict with key: neighbouring vertex
                           value: weight"""
    import collections
    revers_dict = collections.defaultdict(dict)
    for vertex, neighbours_dict in adj.items():
        for neighbour, weight in neighbours_dict.items():
            # to avoid last vertex mapping towards itself
            if  neighbour == vertex and weight == 0:
                continue
            revers_dict[neighbour][vertex] = weight
    # map the end vertex itself
    for vertex in adj:
            if vertex not in revers_dict:
                revers_dict[vertex][vertex] = 0
    return revers_dict

# directed graph without cycle
adj = {'a':{'b':10,'g':3},
              'b':{'c':2},
              'g':{'c':4},
              'c':{'d':4,'f':8},
              'd':{'e':7,'f':4},
              'e':{'e':0},
              'f':{'f':0}}

import pprint
pprint.pprint(dict_reverse(adj))

