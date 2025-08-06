from config import *
from interface import *
import time
from root import root


# VARIABLE
current_node = 0
nodes = list()
nodes_adj = list(set())
node_to_xy = dict()
xy_to_node = dict()
couple_node_for_path = list()
pos_to_widget_case = dict()
current_insertion = 'n' # 'n' for node / 'p' for path


def on_case_cliked(col, row, event):
    if current_insertion == 'n':
        handle_node_insertion(col, row, event)
    else:
        handle_path_insertion(col, row, event)

def handle_node_insertion(col, row, event):
    global current_node, xy_to_node
    event.widget.config(bg=black_1)
    if xy_to_node.get((col,row), 'f') != 'f':
        return
    nodes.append(current_node)
    nodes_adj.append(set())
    node_to_xy[current_node] = tuple((col,row))
    xy_to_node[tuple((col,row))] = current_node
    current_node += 1

def handle_path_insertion(col, row, event):
    global couple_node_for_path
    if xy_to_node.get((col, row), 'f') == 'f':
        return
    if (len(couple_node_for_path) == 1) and (couple_node_for_path[0] == (col, row)):
        del couple_node_for_path[:]
        return
    couple_node_for_path.append((col,row))
    # print(couple_node_for_path)
    if len(couple_node_for_path) == 2:
        nodes_adj[xy_to_node.get(couple_node_for_path[0])].add(xy_to_node.get(couple_node_for_path[1]))
        nodes_adj[xy_to_node.get(couple_node_for_path[1])].add(xy_to_node.get(couple_node_for_path[0]))
        trace_path(couple_node_for_path[0], couple_node_for_path[1], "red", 0.005)
        couple_node_for_path = list()

def  trace_path(node_pos_1, node_pos_2, color_path, sleep_time_s):
    if node_pos_1[0] == node_pos_2[0]:
        start = node_pos_1[1] if node_pos_1[1] < node_pos_2[1] else node_pos_2[1]
        end = node_pos_2[1] if start == node_pos_1[1] else node_pos_1[1]
        for row in range(start + 1, end):
            f = pos_to_widget_case.get((node_pos_1[0],  row))
            f.config(bg=color_path)
            root.update()
            time.sleep(sleep_time_s)
    elif node_pos_1[1] == node_pos_2[1]:
        start = node_pos_1[0] if node_pos_1[0] < node_pos_2[0] else node_pos_2[0]
        end = node_pos_2[0] if start == node_pos_1[0] else node_pos_1[0]
        for col in range(start + 1, end):
            f = pos_to_widget_case.get((col, node_pos_1[1]))
            f.config(bg=color_path)
            root.update()
            time.sleep(sleep_time_s)
    elif abs(node_pos_1[0] - node_pos_2[0]) == abs(node_pos_1[1] - node_pos_2[1]):
        i = - (node_pos_1[0] - node_pos_2[0]) / abs(node_pos_1[0] - node_pos_2[0])
        j = - (node_pos_1[1] - node_pos_2[1]) / abs(node_pos_1[1] - node_pos_2[1])
        start_i = node_pos_1[0] + i
        start_j = node_pos_1[1] + j

        for k in range(abs(node_pos_1[0] - node_pos_2[0]) - 1):
            f = pos_to_widget_case.get((start_i, start_j))
            f.config(bg=color_path)
            start_i = start_i + i
            start_j = start_j + j
            root.update()
            time.sleep(sleep_time_s)
    else:
        i = - (node_pos_1[0] - node_pos_2[0]) / abs(node_pos_1[0] - node_pos_2[0])
        start_i = node_pos_1[0] + i
        for k in range(abs(node_pos_1[0] - node_pos_2[0])):
            f = pos_to_widget_case.get((start_i, node_pos_1[1]))
            f.config(bg=color_path)
            start_i = start_i + i
            root.update()
            time.sleep(sleep_time_s)
        j = - (node_pos_1[1] - node_pos_2[1]) / abs(node_pos_1[1] - node_pos_2[1])
        start_j = node_pos_1[1] 
        for k in range(abs(node_pos_1[1] - node_pos_2[1])):
            f = pos_to_widget_case.get((start_i - i, start_j))
            f.config(bg=color_path)
            start_j = start_j + j
            root.update()
            time.sleep(sleep_time_s)

def test(node_a, node_b):
    trace_path(node_to_xy.get(node_a), node_to_xy.get(node_b), "green", 1)

def toggle_insertion(insert_name_char):
    global current_insertion
    current_insertion = insert_name_char


def search_e_path(event):
    # print(f"{nodes_adj} {nodes}")
    for node in nodes:
        print(f"{node}: {list(nodes_adj[node])}")
        add_adj(node, list(nodes_adj[node]))
    print(find_euler_path(nodes))
    
    
def search_h_path(event):
    print("hamiltonian")