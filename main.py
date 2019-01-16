import tkinter as tk
from tkinter import ttk
import actions

root = tk.Tk()
root.iconbitmap(default="favicon.ico")
root.title("OneNote Helper")
root.geometry("550x100")
root.wm_attributes("-topmost", 1)
frame = tk.Frame(root)
frame.pack()

copy_icon=tk.PhotoImage(file='icons/copy.png')
copy = ttk.Button(frame, image=copy_icon)
copy.pack(side = tk.LEFT)
copy.bind('<Button-1>', actions.copy)

cut_icon=tk.PhotoImage(file='icons/cut.png')
cut = ttk.Button(frame, image=cut_icon)
cut.pack(side = tk.LEFT)
cut.bind('<Button-1>', actions.cut)

paste_icon=tk.PhotoImage(file='icons/paste.png')
paste = ttk.Button(frame, image=paste_icon)
paste.pack(side = tk.LEFT)
paste.bind('<Button-1>', actions.paste)

undo_icon=tk.PhotoImage(file='icons/undo.png')
undo = ttk.Button(frame, image=undo_icon)
undo.pack(side = tk.LEFT)
undo.bind('<Button-1>', actions.undo)

redo_icon=tk.PhotoImage(file='icons/redo.png')
redo = ttk.Button(frame, image=redo_icon)
redo.pack(side = tk.LEFT)
redo.bind('<Button-1>', actions.redo)

root.mainloop()