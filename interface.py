from ctypes import *
import os

# init
path = os.getcwd()
_mylib = CDLL(os.path.join(path, "lib/graph.so"))

# define custome type
class KV_ITEM(Structure):
    _fields_= [
        ("key", c_size_t),
        ("value", POINTER(c_size_t))
    ]

# define type params and retuned function
_mylib.arr_put.argtypes = [POINTER(POINTER(c_size_t)), c_size_t]
_mylib.arr_get.argtypes = [POINTER(POINTER(c_size_t)), c_size_t]
_mylib.arr_free.argtypes = [POINTER(POINTER(c_size_t))]
_mylib.hm_put.argtypes = [POINTER(POINTER(KV_ITEM)), c_size_t, POINTER(c_size_t)]
_mylib.free_graph.argtypes = [POINTER(POINTER(KV_ITEM))]
_mylib.EulerPathByFleury.argtypes = [POINTER(KV_ITEM), POINTER(c_size_t), c_size_t]
_mylib.EulerPathByFleury.restype = POINTER(c_size_t)
_mylib.HamiltonienPathByFleury.argtypes = [POINTER(KV_ITEM), POINTER(c_size_t), c_size_t]
_mylib.HamiltonienPathByFleury.restype = POINTER(c_size_t)

# init graph
adj = POINTER(KV_ITEM)()
item = POINTER(c_size_t)()
euler_chemin = POINTER(c_size_t)()
hamiltonian_chemin = POINTER(c_size_t)()

# function
def add_adj(node, list_adj):
    item = POINTER(c_size_t)()
    for i in list_adj:
        _mylib.arr_put(item, i)
    _mylib.hm_put(adj, node, item)

def find_euler_path(list_node):
    global euler_chemin
    euler_chemin = _mylib.EulerPathByFleury(adj, (c_size_t * len(list_node))(*list_node), len(list_node))
    return euler_chemin[:len(list_node) + 1]

def find_hamiltonian_path(list_node):
    global hamiltonian_chemin
    hamiltonian_chemin = _mylib.HamiltonienPathByFleury(adj, (c_size_t * len(list_node))(*list_node), len(list_node))
    return hamiltonian_chemin[:len(list_node) + 1]


def print_path(path):
    for i in range(_mylib.arr_len(path)):
        print(f"i = {i}, node: {_mylib.arr_get(path, i)}")

        
add_adj(0, [4])
add_adj(1, [2, 3, 4])
add_adj(2, [1, 3])
add_adj(3, [1, 2, 4])
add_adj(4, [0, 1, 3])

print_path(find_euler_path([0, 1, 2, 3, 4]))

# free
_mylib.free_graph(adj)
_mylib.arr_free(euler_chemin)
print(_mylib)