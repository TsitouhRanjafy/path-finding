from config import *

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

def handle_path_insertion(col, row, event):
    global couple_node_for_path
    if not xy_to_node.get((col, row), False):
        return
    if (len(couple_node_for_path) == 1) and (couple_node_for_path[0] == (col, row)):
        del couple_node_for_path[:]
        return
    couple_node_for_path.append((col,row))
    if len(couple_node_for_path) == 2:
        trace_path(couple_node_for_path[0], couple_node_for_path[1])
        couple_node_for_path = list()


def  trace_path(node_pos_1, node_pos_2):
    if node_pos_1[0] == node_pos_2[0]:
        start = node_pos_1[1] if node_pos_1[1] < node_pos_2[1] else node_pos_2[1]
        end = node_pos_2[1] if start == node_pos_1[1] else node_pos_1[1]
        for row in range(start + 1, end):
            f = pos_to_widget_case.get((node_pos_1[0],  row))
            f.config(bg="red")
    elif node_pos_1[1] == node_pos_2[1]:
        start = node_pos_1[0] if node_pos_1[0] < node_pos_2[0] else node_pos_2[0]
        end = node_pos_2[0] if start == node_pos_1[0] else node_pos_1[0]
        for col in range(start + 1, end):
            f = pos_to_widget_case.get((col, node_pos_1[1]))
            f.config(bg="red")
    elif abs(node_pos_1[0] - node_pos_2[0]) == abs(node_pos_1[1] - node_pos_2[1]):
        i = - (node_pos_1[0] - node_pos_2[0]) / abs(node_pos_1[0] - node_pos_2[0])
        j = - (node_pos_1[1] - node_pos_2[1]) / abs(node_pos_1[1] - node_pos_2[1])
        start_i = node_pos_1[0] + i
        start_j = node_pos_1[1] + j

        print(f"start: {start_i}, {start_j} to {node_pos_2[0]}, {node_pos_2[1]} | {i},{j}")
        for k in range(abs(node_pos_1[0] - node_pos_2[0]) - 1):
            f = pos_to_widget_case.get((start_i, start_j))
            f.config(bg="red")
            start_i = start_i + i
            start_j = start_j + j
    else:
        pass


def handle_node_insertion(col, row, event):
    global current_node, xy_to_node
    event.widget.config(bg=black_1)
    if xy_to_node.get((col,row), False):
        return
    current_node += 1
    nodes.append(current_node)
    nodes_adj.append({})
    node_to_xy[current_node] = tuple((col,row))
    xy_to_node[tuple((col,row))] = current_node
    print(f"{nodes} : {node_to_xy}")
    print(f"{nodes} : {nodes_adj}")

def toggle_insertion(insert_name_char):
    global current_insertion
    current_insertion = insert_name_char
    print(f"{current_insertion}")