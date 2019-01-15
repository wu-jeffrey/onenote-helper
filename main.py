import tkinter as tk
from tkinter import ttk
from pynput.keyboard import Key, Controller

keyboard = Controller()

def keypress(event):
    """Simulate Keypress or Macro"""
    keyboard.press('a')
    print("bang")

root = tk.Tk()
root.iconbitmap(default="icon.ico")
root.title("OneNote Helper")
root.geometry("500x100")
root.wm_attributes("-topmost", 1)

frame = tk.Frame(root)
frame.pack()

button = ttk.Button(frame, text='COPY')              
button.pack()
button.bind('<Button-1>', keypress)

root.mainloop()

