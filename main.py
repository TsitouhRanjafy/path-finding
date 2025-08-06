from tkinter import *
from config import *
from helper import *
import helper

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

def on_leave(event, col, row):
    global node_to_xy, xy_to_node, tmp_color
    if xy_to_node.get((col,row), 'f') != 'f':
        return
    event.widget['background'] = tmp_color
    tmp_color = ()

tmp_color = ()
def on_enter(event, col, row):
    global node_to_xy, xy_to_node, tmp_color
    if xy_to_node.get((col,row), 'f') != 'f':
        return
    tmp_color = event.widget.cget("background")
    event.widget['background'] = white_2

def create_case():
    for j in range(count_h):
        for i in range(count_w):
            f = Frame(graph_frame, bg=white_1, height=CASE_SIZE, width=CASE_SIZE, highlightcolor=black_2, highlightthickness=border_1)
            f.grid(column=i, row=j, sticky=NSEW)
            f.bind("<Button-1>", lambda event, frame=f, col_index=i, row_index=j: (on_case_cliked(col_index, row_index, event)))
            f.bind("<Enter>", lambda event, col_index=i, row_index=j: on_enter(event, col_index, row_index))
            f.bind("<Leave>", lambda event, col_index=i, row_index=j: on_leave(event, col_index, row_index))
            pos_to_widget_case[(i, j)] = f

def reinit(event):
    for frame in graph_frame.winfo_children():
        frame.destroy()  
    helper.current_node = 0
    del nodes[:]
    del nodes_adj[:]
    node_to_xy.clear()
    xy_to_node.clear()
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
o1 = Frame(outils_frame, height=100, width=100, bg=black_1, padx=10, pady=5)
o1.rowconfigure((0,1), weight=1)
o1.grid(column=0, row=0, sticky=NSEW)

o1_f1 = Frame(o1)
o1_f1.pack(fill=X, expand=True)
o1_f1_f_insert = Frame(o1_f1, height=30, width=100, bg=white_1)
o1_f1_f_insert.pack(fill=Y)
label = Label(o1_f1_f_insert, text="insert", font=("Arial", 10))
label.pack()

o1_f2 = Frame(o1)
o1_f2.columnconfigure((0,1), weight=1)
o1_f2.pack(fill=X, expand=True)
o1_f2_btn_node = Button(o1_f2, text="node", font=("Arial", 13), width=5, height=1)
o1_f2_btn_node.bind("<Button-1>", lambda event: toggle_insertion('n'))
o1_f2_btn_node.grid(column=0, row=0, sticky=NSEW)

o1_f2_btn_path = Button(o1_f2, text="path", font=("Arial", 13), width=5, height=1)
o1_f2_btn_path.bind("<Button-1>", lambda eveng: toggle_insertion('p'))
o1_f2_btn_path.grid(column=1, row=0, sticky=NSEW)

o2 = Frame(outils_frame, height=100, width=100, bg=black_1)
o2.grid(column=1, row=0, sticky=NSEW)

o3 = Frame(outils_frame, height=100, width=100, bg=black_1)
o3.grid(column=2, row=0, sticky=NSEW)

# Check case
o4 = Frame(outils_frame, height=100, width=100, bg=black_1, padx=10, pady=5)
o4.grid(column=3, row=0, sticky=NSEW)

o4_f1 = Frame(o4)
o4_f1.pack(fill=X, expand=True)
o4_f1_f_insert = Frame(o4_f1, height=30, width=100, bg=white_1)
o4_f1_f_insert.pack(fill=Y)
label = Label(o4_f1_f_insert, text="search", font=("Arial", 10))
label.pack()

o4_f2 = Frame(o4)
o4_f2.columnconfigure((0,1), weight=1)
o4_f2.pack(fill=X, expand=True)
o4_f2_btn_node = Button(o4_f2, text="connex", font=("Arial", 13), width=5, height=1)
o4_f2_btn_node.grid(column=0, row=0, sticky=NSEW)

o4_f2_btn_path = Button(o4_f2, text="euler path", font=("Arial", 13), width=5, height=1)   
o4_f2_btn_path.grid(column=1, row=0, sticky=NSEW)

root.mainloop()
