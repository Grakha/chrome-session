#!/usr/bin/env python3
import tkinter as tk
from tkinter import filedialog

# Main window
window = tk.Tk()

# Title of Frame
window.title('Files Save')

# Size of window
window.geometry("370x340")

# window.withdraw()


# Functions for Choose Paths
def base_path():
    tk.Label(window, text="Base Path").pack()
    file_path = filedialog.askdirectory()

def output_path():
    tk.Label(window, text="Output Path").pack()
    file_path = filedialog.askdirectory()


# Body
title = tk.Label(window, text="Google Save Session", anchor='w').pack(fill='both')

# Path in
label_in = tk.Label(window, text="Input PATH").pack()
entry_in = tk.Entry(window, width="35").pack()

photo = tk.PhotoImage(file="./icons/folder.png")
btn_entry_in = tk.Button(window, image=photo, width="16", height="16", command=base_path).pack()

# Path out
label_out = tk.Label(window, text="Output PATH").pack()
entry_out = tk.Entry(window, width="35").pack()

btn_entry_out = tk.Button(window, image=photo, width="16", height="16", command=output_path).pack()


# buttons
btn_cancel = tk.Button(window, text="Cancel").pack()

btn_ch_path = tk.Button(window, text="Change PATH").pack()

btn_save = tk.Button(window, text="Save").pack()

btn_cp = tk.Button(window, text="Copy").pack()

# Tkinter event loop
window.mainloop()