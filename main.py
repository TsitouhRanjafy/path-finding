from tkinter import *
from tkinter import ttk
from config import *
from helper import *

CASE_SIZE = 10
OUTILS_SIZE = 100
root_w = 700
root_h = 400
count_w = int(root_w / CASE_SIZE)
count_h = int((root_h - OUTILS_SIZE) / CASE_SIZE)

print(f"{count_w} {count_h}")
def on_resize(event):
    global root_w, root_h, count_w
    root_w, root_h = event.width, event.height
    graph_frame.configure(height=root_h - OUTILS_SIZE)

def create_case():
    for j in range(count_h):
        for i in range(count_w):
            f = Frame(graph_frame, bg=white_1, height=CASE_SIZE, width=CASE_SIZE, highlightcolor=black_2, highlightthickness=border_1)
            f.grid(column=i, row=j, sticky=NSEW)
            # label = Label(f, text=f"{i+j}", bg=white_1, font=("Arial", 6))
            # label.pack(fill="both", expand=True)

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
