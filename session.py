#!/usr/bin/env python3
import tkinter as tk
from tkinter import filedialog
import os

# Main window
window = tk.Tk()

# Title of Frame
window.title('Files Save')

# Size of window
window.geometry("370x340")

# window.withdraw()


# Functions for Choose Paths
def close_window():
    window.destroy()

# Body
title = tk.Label(window, text="Google Save Session", anchor='w').pack(fill='both')

photo = tk.PhotoImage(file="./icons/folder.png")



# def initial_dir():
#     dir_path = filedialog.askdirectory(initialdir=entry_path_in, title="Select Folder Where Files is")
#     if dir_path:
#         entry_in.delete('0', 'end')
#         entry_in.insert(0, dir_path)
        
    # entry_path_in = dir_path

# def output_dir():
#     dir_path = filedialog.askdirectory(initialdir=entry_path_out, title="Select Folder Where Save Files")
#     if dir_path:
#         entry_out.delete('0', 'end')
#         entry_out.insert(0, dir_path)
    # entry_path_out = dir_path

class SelectDir:

    def __init__(self, dir_in, dir_out):
        self.dir_in = dir_in
        self.dir_out = dir_out
        self.label_in = "Select Folder Where Files is"
        self.label_out = "Select Folder Where Save Files"

    def initial_dir(self):
        path_name = filedialog.askdirectory(initialdir=self.dir_in, title=self.label_in)
        print(path_name)
        if path_name:
            entry_in.delete('0', 'end')
            entry_in.insert(0, path_name)
            self.dir_in = path_name

    def output_dir(self):
        path_name = filedialog.askdirectory(initialdir=self.dir_out, title=self.label_out)
        if path_name:
            entry_out.delete('0', 'end')
            entry_out.insert(0, path_name)
            self.dir_out = path_name


# Path in
label_in = tk.Label(window, text="Input PATH").pack()
entry_in = tk.Entry(window, width="35")
entry_path_in = entry_in.insert(0, 'C:/')
entry_in.pack()

# Path out
label_out = tk.Label(window, text="Output PATH").pack()
entry_out = tk.Entry(window, width="35")
entry_path_out = entry_out.insert(0, 'D:/')
entry_out.pack()

btn_init = SelectDir(entry_in.get(), entry_out.get())

tk.Button(window, image=photo, width="16", height="16", command=btn_init.initial_dir).pack()

tk.Button(window, image=photo, width="16", height="16", command=btn_init.output_dir).pack()



# buttons
btn_cancel = tk.Button(window, text="Cancel", command=close_window).pack()

btn_ch_path = tk.Button(window, text="Change PATH").pack()

btn_save = tk.Button(window, text="Save").pack()

btn_cp = tk.Button(window, text="Copy").pack()

# Tkinter event loop
window.mainloop()