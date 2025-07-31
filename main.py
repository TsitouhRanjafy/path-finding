from tkinter import *
from tkinter import ttk
from config import *

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
    current_node += 1
    nodes.append(current_node)
    pos_node[current_node] = tuple((col,row))
    print(f"{nodes} : {pos_node}")

def create_case():
    for j in range(count_h):
        for i in range(count_w):
            f = Frame(graph_frame, bg=white_1, height=CASE_SIZE, width=CASE_SIZE, highlightcolor=black_2, highlightthickness=border_1)
            f.grid(column=i, row=j, sticky=NSEW)
            f.bind("<Button-1>", lambda event, frame=f, col_index=i, row_index=j:((frame.config(bg=black_1)), on_case_cliked(col_index, row_index)))
            # label = Label(f, text=f"{i+j}", bg=white_1, font=("Arial", 6))
            # label.pack(fill="both", expand=True)
    reinit_btn = Button(graph_frame, width=1, height=1, bg="red")
    reinit_btn.place(x=10, y=10)
    reinit_btn.bind("<Button-1>", reinit)

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

create_case()


# OUTILS FRAME
outils_frame = Frame(root, bg=black_1, height=OUTILS_SIZE,highlightcolor=black_2, highlightthickness=border_1)
outils_frame.pack(side="top", fill=X)

root.mainloop()
