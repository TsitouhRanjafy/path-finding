from config import *
from interface import *
import time
from root import root
from tkinter import DoubleVar, StringVar


current_node = 0
nodes = list()
nodes_adj = list(set())
path_count = 0
node_to_xy = dict()
xy_to_node = dict()
couple_node_for_path = list()
pos_to_widget_case = dict()
current_insertion = 'n' # 'n' for node / 'p' for path
spin_val = DoubleVar()
spin_val.set(5)
status = StringVar()
status.set("")
status_label = {}


def on_case_cliked(col, row, event):
    if current_insertion == 'n': handle_node_insertion(col, row, event)
    else: handle_path_insertion(col, row, event)

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
    global couple_node_for_path, path_count
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
        trace_path(couple_node_for_path[0], couple_node_for_path[1], "red", 0.005, True, False)
        couple_node_for_path = list()
        path_count += 1

def  trace_path(node_pos_1, node_pos_2, color_path, sleep_time_s, is_insertion, is_travel):
    if node_pos_1[0] == node_pos_2[0]:
        trace_path_v_or_h(node_pos_1, node_pos_2, color_path, sleep_time_s, 1, is_travel)
    elif node_pos_1[1] == node_pos_2[1]:
        trace_path_v_or_h(node_pos_1, node_pos_2, color_path, sleep_time_s, 0, is_travel)
    elif abs(node_pos_1[0] - node_pos_2[0]) == abs(node_pos_1[1] - node_pos_2[1]):
        trace_path_diagonals(node_pos_1, node_pos_2, color_path, sleep_time_s,is_travel)
    else:
        axe = 0
        if xy_to_node.get((node_pos_2[0], node_pos_1[1]), 'f') != 'f': # eviter de colorer le node en rouge (couleur du path)
            axe = 1
        if is_insertion:
            trace_path_random_node(node_pos_1, node_pos_2, color_path, sleep_time_s, axe, is_travel)
        else:
            i = - (node_pos_1[axe] - node_pos_2[axe]) / abs(node_pos_1[axe] - node_pos_2[axe])
            start_i = node_pos_1[axe] + i
            f_tmp = pos_to_widget_case.get((start_i, node_pos_1[1]))
            
            if f_tmp['background'] != "red": # eviter de colorer le chemin qui n'est pas rouge
                axe = 1
            trace_path_random_node(node_pos_1, node_pos_2, color_path, sleep_time_s, axe, is_travel)
            pass

def trace_path_v_or_h(node_pos_1, node_pos_2, color_path, sleep_time_s, axe, is_travel):
    f = ()
    j = - (node_pos_1[axe] - node_pos_2[axe]) / abs(node_pos_1[axe] - node_pos_2[axe])
    start_j = node_pos_1[axe] + j
    for tmp in range(abs(node_pos_1[axe] - node_pos_2[axe]) - 1):
        if axe == 0:
            f = pos_to_widget_case.get((start_j, node_pos_1[1]))
        else:
            f = pos_to_widget_case.get((node_pos_1[0],  start_j))
        f.config(bg=color_path)
        start_j = start_j + j
        root.update()
        time.sleep(sleep_time_s)
        if is_travel:
            f.config(bg="red")

def trace_path_diagonals(node_pos_1, node_pos_2, color_path, sleep_time_s, is_travel):
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
        if is_travel:
            f.config(bg="red")

def trace_path_random_node(node_pos_1, node_pos_2, color_path, sleep_time_s, axe, is_travel):
    f = ()
    i = - (node_pos_1[axe] - node_pos_2[axe]) / abs(node_pos_1[axe] - node_pos_2[axe])
    start_i = node_pos_1[axe] + i
    for k in range(abs(node_pos_1[axe] - node_pos_2[axe])):
        if axe == 0:
            f = pos_to_widget_case.get((start_i, node_pos_1[1]))
        else:
            f = pos_to_widget_case.get((node_pos_1[0], start_i))
        f.config(bg=color_path)
        start_i = start_i + i
        root.update()
        time.sleep(sleep_time_s)
        if is_travel:
            f.config(bg="red")
    axe = (axe + 1) %  2
    j = - (node_pos_1[axe] - node_pos_2[axe]) / abs(node_pos_1[axe] - node_pos_2[axe])
    start_j = node_pos_1[axe] 
    for k in range(abs(node_pos_1[axe] - node_pos_2[axe])):
        if axe == 0:
            f = pos_to_widget_case.get((start_j, start_i - i))
        else:
            f = pos_to_widget_case.get((start_i - i, start_j))
        f.config(bg=color_path)
        start_j = start_j + j
        root.update()
        time.sleep(sleep_time_s)
        if is_travel:
            f.config(bg="red")

def toggle_insertion(insert_name_char):
    global current_insertion
    current_insertion = insert_name_char

def search_e_path(event):
    global path_count
    if len(nodes) == 0:
        set_status("insert node first", False)
        return
    for node in nodes:
        add_adj(node, list(nodes_adj[node]))
    path = find_euler_path(nodes)
    if (len(path) - 1) != path_count: set_status("not found", False)
    else: set_status("ok", True)

    if len(path) == 0:
        return
    a = path[0]
    i = 1
    while i < len(path):
        trace_path(node_to_xy.get(a), node_to_xy.get(path[i]), "green", round((spin_val.get() * 0.01), 2), False, False)
        a = path[i]
        i += 1
    
def search_h_path(event):
    if len(nodes) == 0:
        set_status("insert node first", False)
        return
    for node in nodes:
        add_adj(node, list(nodes_adj[node]))
    max_path = find_hamiltonian_path(nodes, 0)
    for i in range(1, len(nodes)):
        path = find_hamiltonian_path(nodes, i)
        if len(max_path) < len(path):
            max_path = path
    
    if len(max_path) != len(nodes): set_status("not found", False)
    else: set_status("ok", True)

    if len(max_path)== 0:
        return
    a = max_path[0]
    f = pos_to_widget_case.get((node_to_xy.get(a)))
    f.config(bg="blue")
    i = 1
    while i < len(max_path):
        trace_path(node_to_xy.get(a), node_to_xy.get(max_path[i]), "green", round((spin_val.get() * 0.01), 2), False, True)
        f = pos_to_widget_case.get((node_to_xy.get(max_path[i])))
        f.config(bg="blue")
        a = max_path[i]
        i += 1

def set_status(message, is_ok):
    status.set(message)
    if is_ok: status_label.get(0).config(fg="green") 
    else: status_label.get(0).config(fg="red")