#!/usr/bin/env python3
import tkinter as tk
from tkinter import filedialog, ttk
from win10toast import ToastNotifier
import os
import shutil

# Windows ToastNotifier init
notify = ToastNotifier()

# Main window
window = tk.Tk()
window.resizable(0, 0)

# Title of Frame
window.title('Files and Folders')

# Window Photo
window.iconphoto(False, tk.PhotoImage(file="./icons/mv.png"))

# Size of window
window.geometry("420x250")

# window.withdraw()
# Body
tk.Label(window, text="Save Sessions & Tabs", anchor='w', font=('Arial', 12)).grid(columnspan=3, pady=15)

photo = tk.PhotoImage(file="./icons/folder.png")
pic_x = tk.PhotoImage(file="./icons/x.png")

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

    def popup_msg(self):
        popup = tk.Tk()
        popup.iconbitmap("./icons/att.ico")
        popup.resizable(0, 0)
        popup.geometry("280x105")
        popup.wm_title("Permission Denied.")
        ttk.Label(popup, text="Please close Browser").pack(padx=15, pady=15)
        ttk.Button(popup, text="Okey", command=popup.destroy).pack(padx=10, pady=10)
        popup.mainloop()

    def copy_file(self):
        try:
            for item in os.listdir(self.src):
                if item.endswith('Session') or item.endswith('Tabs'):
                    file_name = os.path.join(os.path.normpath(self.src), item)
                    shutil.copy(file_name, self.dst)

            notify.show_toast(
                "Copy Files",
                "Files successfully copied",
                duration=5, icon_path="./icons/copy.ico", threaded=True)

        except PermissionError:
            self.popup_msg()
        except:
            print("Error occurred while copying file.")


    def clear_in(self):
        self.src = entry_in.delete('0', 'end')
        self.src = entry_in.insert(0, 'C:/')

    def clear_out(self):
        self.dst = entry_out.delete('0', 'end')
        self.dst = entry_out.insert(0, 'D:/')

    def close_window(self):
        window.destroy()



# Input src
tk.Label(window, text="Browse Directory").grid(row=1, column=0, sticky='w', padx=10)
entry_in = tk.Entry(window, width=47, font=('Arial', 10))
entry_in.insert(0, 'C:/')
entry_in.grid(row=2, column=0, padx=10, pady=5)

# Input dst
tk.Label(window, text="Destination Directory").grid(row=3, column=0, sticky='w', padx=10)
entry_out = tk.Entry(window, width=47, font=('Arial', 10))
entry_out.insert(0, 'D:/')
entry_out.grid(row=4, column=0, padx=10, pady=5)

btn_init = SelectDir(entry_in.get(), entry_out.get())

# buttons
tk.Button(window, image=photo, width=15, height=15, command=btn_init.browse_folder).grid(row=2, column=2, padx=5, pady=5)
tk.Button(window, image=pic_x, width=15, height=15, command=btn_init.clear_in).grid(row=2, column=3, padx=5, pady=5)
tk.Button(window, image=photo, width=15, height=15, command=btn_init.move_to).grid(row=4, column=2, padx=5, pady=5)
tk.Button(window, image=pic_x, width=15, height=15, command=btn_init.clear_out).grid(row=4, column=3, padx=5, pady=5)

tk.Button(window, text="Copy", width=7, command=btn_init.copy_file).place(relx=0.68, rely=0.8)
tk.Button(window, text="Close", width=7, command=btn_init.close_window).place(relx=0.84, rely=0.8)

# Tkinter event loop
window.mainloop()