import tkinter as tk
root = tk.Tk()
root.wm_attributes("-topmost", 1)

w = tk.Label(root, text="DERP Tkinter!")
w.pack()

root.mainloop()