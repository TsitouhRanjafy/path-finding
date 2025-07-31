from tkinter import *
from tkinter import ttk
from config import *
import math

# PROPERTY
CASE_SIZE = 10
OUTILS_SIZE = 100
root_w = 700
root_h = 400
count_w = int(root_w / CASE_SIZE)
count_h = int((root_h - OUTILS_SIZE) / CASE_SIZE)

# FUNCTION
def on_resize(event):
    global root_w, root_h, count_w
    root_w, root_h = event.width, event.height
    graph_frame.configure(height=root_h - OUTILS_SIZE)

current_node = 0
nodes = list()
pos_node = dict()
def on_case_cliked(col, row):
    global current_node
    if tuple((col,row)) in pos_node.values():
        return
    current_node += 1
    nodes.append(current_node)
    pos_node[current_node] = tuple((col,row))
    print(f"{nodes} : {pos_node}")

def on_leave(event, col, row):
    global pos_node
    if (col, row) in pos_node.values():
        return
    event.widget['background'] = white_1

def on_enter(event, col, row):
    global pos_node
    if (col, row) in pos_node.values():
        return
    event.widget['background'] = white_2

def create_case():
    for j in range(count_h):
        for i in range(count_w):
            f = Frame(graph_frame, bg=white_1, height=CASE_SIZE, width=CASE_SIZE, highlightcolor=black_2, highlightthickness=border_1)
            f.grid(column=i, row=j, sticky=NSEW)
            f.bind("<Button-1>", lambda event, frame=f, col_index=i, row_index=j:((frame.config(bg=black_1)), on_case_cliked(col_index, row_index)))
            f.bind("<Enter>", lambda event, col_index=i, row_index=j: on_enter(event, col_index, row_index))
            f.bind("<Leave>", lambda event, col_index=i, row_index=j: on_leave(event, col_index, row_index))

def reinit(event):
    global current_node
    for frame in graph_frame.winfo_children():
        frame.destroy()  
    current_node = 0
    del nodes[:]
    pos_node.clear()
    create_case()  

# MAIN FRAME
root = Tk()
root.configure(bg=white_1, highlightcolor=black_2, highlightthickness=border_1)
root.geometry(f"{root_w}x{root_h}")
root.bind("<Configure>", on_resize)
root.title("Path Finding")


# GRAPH FRAME
graph_frame = Frame(root, bg=white_1, height=root_h - OUTILS_SIZE,highlightcolor=black_2, highlightthickness=border_1)
graph_frame.pack(side="top", fill="both", expand=True)
graph_frame.columnconfigure(tuple(range(0, count_w)), weight=1)
graph_frame.rowconfigure(tuple(range(0, count_h)), weight=1)

# RELOAD BUTTON
icon = PhotoImage(file="reload.png")
reinit_btn = Button(root, width=24, height=24, image=icon, bg=white_1)
reinit_btn.place(x=10, y=10)
reinit_btn.image = icon
reinit_btn.bind("<Button-1>", reinit)

create_case()

# OUTILS FRAME
outils_frame = Frame(root, bg=black_1, background=black_1,height=OUTILS_SIZE,highlightcolor=black_2, highlightthickness=border_1)
outils_frame.pack(fill=X, side="bottom")
outils_frame.columnconfigure((0,3), weight=1)
outils_frame.rowconfigure(0, weight=1)

# Insert case
o1 = Frame(outils_frame, height=100, width=100, bg=black_1, highlightbackground="red", highlightthickness=1, padx=10, pady=5)
o1.rowconfigure((0,1), weight=1)
o1.grid(column=0, row=0, sticky=NSEW)

o1_f1 = Frame(o1, highlightbackground="green", highlightthickness=1)
o1_f1.pack(fill=X, expand=True)
o1_f1_f_insert = Frame(o1_f1, height=30, width=100, bg=white_1)
o1_f1_f_insert.pack(fill=Y)
label = Label(o1_f1_f_insert, text="insert", font=("Arial", 13))
label.pack()

o1_f2 = Frame(o1, highlightbackground="green", highlightthickness=1)
o1_f2.columnconfigure((0,1), weight=1)
o1_f2.pack(fill=X, expand=True)
o1_f2_btn_node = Button(o1_f2, width=5, height=1)
o1_f2_btn_node_label = Label(o1_f2_btn_node, text="node", font=("Arial", 16))
o1_f2_btn_node_label.pack()
o1_f2_btn_node.grid(column=0, row=0, sticky=NSEW)

o1_f2_btn_path = Button(o1_f2, width=5, height=1, padx=1)
o1_f2_btn_path_label = Label(o1_f2_btn_path , text="path", font=("Arial", 16))
o1_f2_btn_path_label.pack()
o1_f2_btn_path.grid(column=1, row=0, sticky=NSEW)

o2 = Frame(outils_frame, height=100, width=100, bg=black_1, highlightbackground="red", highlightthickness=1)
o2.grid(column=1, row=0, sticky=NSEW)

o3 = Frame(outils_frame, height=100, width=100, bg=black_1, highlightbackground="red", highlightthickness=1)
o3.grid(column=2, row=0, sticky=NSEW)

# Check case
o4 = Frame(outils_frame, height=100, width=100, bg=black_1, highlightbackground="red", highlightthickness=1)
o4.grid(column=3, row=0, sticky=NSEW)

o4_f1 = Frame(o4, highlightbackground="green", highlightthickness=1)
o4_f1.pack(fill=X, expand=True)
o4_f1_f_insert = Frame(o4_f1, height=30, width=100, bg=white_1)
o4_f1_f_insert.pack(fill=Y)
label = Label(o4_f1_f_insert, text="search", font=("Arial", 13))
label.pack()

o4_f2 = Frame(o4, highlightbackground="green", highlightthickness=1)
o4_f2.columnconfigure((0,1), weight=1)
o4_f2.pack(fill=X, expand=True)
o4_f2_btn_node = Button(o4_f2, width=5, height=5)
o4_f2_btn_node_label = Label(o4_f2_btn_node, text="connex", font=("Arial", 16))
o4_f2_btn_node_label.pack(expand=True)
o4_f2_btn_node.grid(column=0, row=0, sticky=NSEW)

o4_f2_btn_path = Button(o4_f2, width=5, height=5)   
o4_f2_btn_path_label = Label(o4_f2_btn_path , text="euler path", font=("Arial", 16))
o4_f2_btn_path_label.pack(expand=True)
o4_f2_btn_path.grid(column=1, row=0, sticky=NSEW)

root.mainloop()
