import collections
# bsf by using dque, return all keys in bsf order
def BFS(vertex, adj_dict):
    que_list = collections.deque([vertex])
    parent_dict = {vertex:None}
    bsf_list=[vertex]
    while que_list:
        parent = que_list.popleft()
        for element in adj_dict[parent]:
            if element not in parent_dict:
                que_list.append(element)
                parent_dict[element]=parent
                bsf_list.append(element)
    return bsf_list, parent_dict

# undirected graph with cycle
adj_dict_1 = {'a':['s','z'],
            's':['a','x'],
            'z':['a'],
            'x':['s','d','c'],
            'd':['x','c','f'],
            'c':['d','x','f','v'],
            'f':['d','c','v'],
            'v':['c','f']}
print(BFS('s',adj_dict_1))
#