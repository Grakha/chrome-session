#!/usr/bin/env python3
import tkinter as tk
from tkinter import filedialog
import os
import shutil

# Main window
window = tk.Tk()

# Title of Frame
window.title('Files Save')

# Size of window
window.geometry("370x340")

# window.withdraw()
# Body
tk.Label(window, text="Google Save Session", anchor='w').pack(fill='both')

photo = tk.PhotoImage(file="./icons/folder.png")

class SelectDir:

    def __init__(self, src, dst):
        self.gui()
        self.src = src
        self.dst = dst
        self.label_in = "Select Folder Where Files is"
        self.label_out = "Select Folder Where Save Files"

    def gui(self):
        pass

    def browse_folder(self):
        src = filedialog.askdirectory(initialdir=self.src, title=self.label_in)
        if src:
            entry_in.delete('0', 'end')
            entry_in.insert(0, src)
            self.src = src

    def move_to(self):
        dst = filedialog.askdirectory(initialdir=self.dst, title=self.label_out)
        if dst:
            entry_out.delete('0', 'end')
            entry_out.insert(0, dst)
            self.dst = dst

    def copy_file(self):
        for item in os.listdir(self.src):
            if item.endswith('Session') or item.endswith('Tabs'):
                file_name = os.path.join(os.path.normpath(self.src), item)
                print(file_name)
                shutil.copy(file_name, self.dst)

    def clear_in(self):
        self.src = entry_in.delete('0', 'end')

    def clear_out(self):
        self.dst = entry_out.delete('0', 'end')

    def close_window(self):
        window.destroy()



# Input src
tk.Label(window, text="Input PATH").pack()
entry_in = tk.Entry(window, width="35")
entry_in.insert(0, 'C:/')
entry_in.pack()

# Input dst
tk.Label(window, text="Output PATH").pack()
entry_out = tk.Entry(window, width="35")
entry_out.insert(0, 'D:/')
entry_out.pack()

btn_init = SelectDir(entry_in.get(), entry_out.get())

# buttons
tk.Button(window, image=photo, width="16", height="16", command=btn_init.browse_folder).pack()
tk.Button(window, text="X", command=btn_init.clear_in).pack()

tk.Button(window, image=photo, width="16", height="16", command=btn_init.move_to).pack()
tk.Button(window, text="X", command=btn_init.clear_out).pack()

tk.Button(window, text="Cancel", command=btn_init.close_window).pack()
tk.Button(window, text="Copy", command=btn_init.copy_file).pack()

# Tkinter event loop
window.mainloop()